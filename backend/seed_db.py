import pandas as pd
from app.core.database import SessionLocal, engine, Base
from app.models.analytics_models import Customer, Product, Order, OrderItem

Base.metadata.create_all(bind=engine)
db = SessionLocal()

try:
    print("Seeding database...")
    
    cust_df = pd.read_csv("../data/customers.csv")
    for _, row in cust_df.iterrows():
        db.add(Customer(**row.to_dict()))
        
    prod_df = pd.read_csv("../data/products.csv")
    for _, row in prod_df.iterrows():
        db.add(Product(**row.to_dict()))
        
    db.commit()

    ord_df = pd.read_csv("../data/orders.csv")
    ord_df['order_date'] = pd.to_datetime(ord_df['order_date'])
    for _, row in ord_df.iterrows():
        db.add(Order(**row.to_dict()))

    items_df = pd.read_csv("../data/order_items.csv")
    for _, row in items_df.iterrows():
        db.add(OrderItem(**row.to_dict()))

    db.commit()
    print("Database successfully seeded with transactions!")
finally:
    db.close()
    