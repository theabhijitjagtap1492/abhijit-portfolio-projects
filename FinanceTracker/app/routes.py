from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
from app.models import Transaction
from app.forms import TransactionForm
from app import db
import pandas as pd
from datetime import datetime
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import tempfile

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Check if user has any income first
    has_income = Transaction.query.filter_by(type='income').first() is not None
    
    if not has_income:
        flash('Please add your income first before adding expenses!', 'warning')
        return redirect(url_for('main.add_transaction'))
    
    # Get all transactions in reverse chronological order
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    
    # Calculate totals
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expenses = sum(t.amount for t in transactions if t.type == 'expense')
    balance = total_income - total_expenses
    
    return render_template('index.html', 
                         transactions=transactions,
                         total_income=total_income,
                         total_expenses=total_expenses,
                         balance=balance)

@main.route('/add', methods=['GET', 'POST'])
def add_transaction():
    form = TransactionForm()
    
    if form.validate_on_submit():
        transaction = Transaction(
            amount=form.amount.data,
            category=form.category.data,
            type=form.type.data,
            description=form.description.data,
            date=form.date.data
        )
        
        db.session.add(transaction)
        db.session.commit()
        
        flash('Transaction added successfully!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('add_transaction.html', form=form)

@main.route('/dashboard')
def dashboard():
    transactions = Transaction.query.all()
    
    if not transactions or all(t.type != 'expense' for t in transactions):
        # No transactions or no expenses: show empty dashboard
        return render_template('dashboard.html',
                              income_total=0,
                              expense_total=0,
                              savings=0,
                              categories=[],
                              expenses_by_category=[])

    # Prepare data for charts
    income_total = sum(t.amount for t in transactions if t.type == 'income')
    expense_total = sum(t.amount for t in transactions if t.type == 'expense')
    savings = income_total - expense_total
    
    # Expenses by category
    expenses_by_category_dict = {}
    for t in transactions:
        if t.type == 'expense':
            if t.category in expenses_by_category_dict:
                expenses_by_category_dict[t.category] += t.amount
            else:
                expenses_by_category_dict[t.category] = t.amount
    
    categories = list(expenses_by_category_dict.keys())
    expenses_by_category = [expenses_by_category_dict[cat] for cat in categories]
    
    return render_template('dashboard.html',
                         income_total=income_total,
                         expense_total=expense_total,
                         savings=savings,
                         categories=categories,
                         expenses_by_category=expenses_by_category)

@main.route('/export')
def export():
    transactions = Transaction.query.all()
    
    # Create DataFrame
    data = []
    for t in transactions:
        data.append({
            'Date': t.date,
            'Type': t.type,
            'Category': t.category,
            'Amount': t.amount,
            'Description': t.description
        })
    
    df = pd.DataFrame(data)
    
    if df.empty or len(df.columns) == 0:
        flash('No data added. Nothing to export.', 'warning')
        return redirect(url_for('main.dashboard'))

    buffer = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    c = canvas.Canvas(buffer.name, pagesize=letter)
    width, height = letter

    c.setFont('Helvetica-Bold', 16)
    c.drawString(40, height - 40, 'Finance Transactions')
    c.setFont('Helvetica', 10)

    # Table data
    table_data = [df.columns.tolist()] + df.values.tolist()
    table = Table(table_data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    table_width, table_height = table.wrapOn(c, width - 80, height - 100)
    table.drawOn(c, 40, height - 80 - table_height)

    c.save()
    buffer.seek(0)

    return send_file(
        buffer.name,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'finance_transactions_{datetime.now().strftime("%Y%m%d")}.pdf'
    )

@main.route('/reset', methods=['POST'])
def reset():
    Transaction.query.delete()
    db.session.commit()
    flash('All transactions have been deleted.', 'success')
    return redirect(url_for('main.index'))

@main.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    form = TransactionForm(obj=transaction)
    if form.validate_on_submit():
        transaction.amount = form.amount.data
        transaction.category = form.category.data
        transaction.type = form.type.data
        transaction.description = form.description.data
        transaction.date = form.date.data
        db.session.commit()
        flash('Transaction updated successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('edit_transaction.html', form=form, transaction=transaction)

@main.route('/delete/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    db.session.delete(transaction)
    db.session.commit()
    flash('Transaction deleted successfully!', 'success')
    return redirect(url_for('main.index')) 