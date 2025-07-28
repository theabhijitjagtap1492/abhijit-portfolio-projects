from app import db
from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'income' or 'expense'
    description = db.Column(db.String(200))
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow().date())
    
    def __repr__(self):
        return f'<Transaction {self.type}: {self.amount} - {self.category}>' 