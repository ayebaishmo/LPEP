from db import db

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    Purchase_history = db.Column(db.Integer, nullable=False)
    loyality_program = db.Column(db.Integer, nullable=False)
    product_purchased = db.Column(db.String(100), nullable=False)
    browsing_history = db.Column(db.Integer, nullable=False)
    search_queries = db.Column(db.Integer, nullable=False)
    social_media_active = db.Column(db.Integer, nullable=False)
    email_open_rate = db.Column(db.Float, nullable=False)
    avg_order_value = db.Column(db.Float, nullable=False)
