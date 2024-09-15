from  flask import Flask, render_template
from data_loader import load_data
from db import db
from models import Customer


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer_database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return render_template('customer.html', customers=customers)


if __name__ == '__main__':
    # with app.app_context():
    #     load_data()\
    
    app.run()

