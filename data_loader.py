import pandas as pd
from db import db
from models import Customer

def load_data():
    df = pd.read_csv('C:/Users/ISHMO_CT/Downloads/my-projects/deep_learning_env/LPEP/Customer_data.csv')

    for index, row in df.iterrows():
        customer= Customer(
            customer_id=row['customer_id'],
            age=row['age'],
            gender=row['gender'],
            location=row['location'],
            Purchase_history=row['Purchase_history'],
            loyality_program=row['loyality_program'],
            product_purchased=row['product_purchased'],
            browsing_history=row['browsing_history'],
            search_queries=row['search_queries'],
            social_media_active=row['social_media_active'],
            email_open_rate=row['email_open_rate'],
            avg_order_value=row['avg_order_value']
        )

        db.session.add(customer)

    db.session.commit()