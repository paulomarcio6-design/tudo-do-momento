from src.models.user import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = 'sales'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    product_name = db.Column(db.String(200), nullable=False)
    sale_price = db.Column(db.Float, nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)
    profit = db.Column(db.Float, nullable=False)
    profit_percentage = db.Column(db.Float, nullable=False)
    buyer_name = db.Column(db.String(200), nullable=False)
    buyer_document = db.Column(db.String(20), nullable=False)  # CPF ou CNPJ
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    product = db.relationship('Product', backref='sales')
    
    def __repr__(self):
        return f'<Sale {self.id} - {self.product_name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'product_name': self.product_name,
            'sale_price': self.sale_price,
            'purchase_price': self.purchase_price,
            'profit': self.profit,
            'profit_percentage': self.profit_percentage,
            'buyer_name': self.buyer_name,
            'buyer_document': self.buyer_document,
            'sale_date': self.sale_date.isoformat() if self.sale_date else None
        }

