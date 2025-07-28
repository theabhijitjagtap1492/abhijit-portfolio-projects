from app import create_app, db
from app.models import Transaction

app = create_app()

with app.app_context():
    print("=== FINANCE TRACKER DATABASE DATA ===\n")
    
    # Get all transactions
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    
    if not transactions:
        print("No transactions found in the database.")
    else:
        print(f"Total transactions: {len(transactions)}\n")
        
        # Calculate totals
        total_income = sum(t.amount for t in transactions if t.type == 'income')
        total_expenses = sum(t.amount for t in transactions if t.type == 'expense')
        balance = total_income - total_expenses
        
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}\n")
        
        print("=== TRANSACTION DETAILS ===")
        print(f"{'ID':<3} {'Date':<12} {'Type':<8} {'Category':<15} {'Amount':<10} {'Description':<30}")
        print("-" * 90)
        
        for t in transactions:
            print(f"{t.id:<3} {t.date.strftime('%Y-%m-%d'):<12} {t.type:<8} {t.category:<15} ${t.amount:<9.2f} {t.description[:28]:<30}")
        
        print("\n=== EXPENSES BY CATEGORY ===")
        expenses_by_category = {}
        for t in transactions:
            if t.type == 'expense':
                if t.category in expenses_by_category:
                    expenses_by_category[t.category] += t.amount
                else:
                    expenses_by_category[t.category] = t.amount
        
        for category, amount in sorted(expenses_by_category.items(), key=lambda x: x[1], reverse=True):
            print(f"{category}: ${amount:.2f}") 