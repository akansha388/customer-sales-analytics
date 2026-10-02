import random
import uuid
from datetime import datetime, timedelta
import pandas as pd

REGIONS = ["North America", "Europe", "Asia-Pacific", "Latin America"]
CATEGORIES = {
    "Electronics": [("Laptop Pro", 1200, 800), ("Wireless Headphones", 150, 70), ("Smartwatch", 250, 120)],
    "Apparel": [("Leather Jacket", 200, 90), ("Running Shoes", 110, 45), ("Denim Jeans", 80, 30)],
    "Home & Kitchen": [("Espresso Machine", 450, 220), ("Blender", 90, 40), ("Air Fryer", 130, 60)]
}

def generate_mock_data(num_customers=100, num_orders=500):
    customers = []
    for i in range(1, num_customers + 1):
        customers.append({
            "id": str(uuid.uuid4()),
            "customer_code": f"CUST-{1000 + i}",
            "name": f"Customer {i}",
            "email": f"customer{i}@example.com",
            "region": random.choice(REGIONS)
        })
    
    products = []
    p_idx = 1
    for cat, items in CATEGORIES.items():
        for p_name, price, cost in items:
            products.append({
                "id": str(uuid.uuid4()),
                "product_code": f"PROD-{100 + p_idx}",
                "name": p_name,
                "category": cat,
                "unit_price": price,
                "unit_cost": cost
            })
            p_idx += 1
            
    orders = []
    order_items = []
    start_date = datetime.now() - timedelta(days=365)
    
    for o_idx in range(1, num_orders + 1):
        cust = random.choice(customers)
        order_date = start_date + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23))
        order_id = str(uuid.uuid4())
        
        num_items = random.randint(1, 4)
        order_total = 0
        
        for _ in range(num_items):
            prod = random.choice(products)
            qty = random.randint(1, 3)
            tot_price = qty * prod["unit_price"]
            profit = tot_price - (qty * prod["unit_cost"])
            order_total += tot_price
            
            order_items.append({
                "id": str(uuid.uuid4()),
                "order_id": order_id,
                "product_id": prod["id"],
                "quantity": qty,
                "unit_price": prod["unit_price"],
                "unit_cost": prod["unit_cost"],
                "total_price": tot_price,
                "profit": profit
            })
            
        orders.append({
            "id": order_id,
            "order_number": f"ORD-{10000 + o_idx}",
            "customer_id": cust["id"],
            "order_date": order_date,
            "total_amount": order_total,
            "region": cust["region"]
        })
        
    return pd.DataFrame(customers), pd.DataFrame(products), pd.DataFrame(orders), pd.DataFrame(order_items)

if __name__ == "__main__":
    cust_df, prod_df, ord_df, items_df = generate_mock_data()
    cust_df.to_csv("data/customers.csv", index=False)
    prod_df.to_csv("data/products.csv", index=False)
    ord_df.to_csv("data/orders.csv", index=False)
    items_df.to_csv("data/order_items.csv", index=False)
    print("Sample datasets created successfully in data/ folder.")