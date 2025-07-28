from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, NumberRange, Optional

class TransactionForm(FlaskForm):
    amount = FloatField('Amount', validators=[
        DataRequired(),
        NumberRange(min=0.01, message='Amount must be greater than 0')
    ])
    
    category = SelectField('Category', validators=[DataRequired()], choices=[
        ('Salary', 'Salary'),
        ('Freelance', 'Freelance'),
        ('Investment', 'Investment'),
        ('Food', 'Food'),
        ('Rent', 'Rent'),
        ('Transportation', 'Transportation'),
        ('Entertainment', 'Entertainment'),
        ('Shopping', 'Shopping'),
        ('Healthcare', 'Healthcare'),
        ('Utilities', 'Utilities'),
        ('Other', 'Other')
    ])
    
    type = SelectField('Type', validators=[DataRequired()], choices=[
        ('income', 'Income'),
        ('expense', 'Expense')
    ])
    
    description = TextAreaField('Description (Optional)', validators=[Optional()])
    date = DateField('Date', validators=[DataRequired()]) 