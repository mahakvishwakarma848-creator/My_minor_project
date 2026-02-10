import pandas as pd
import random
import time
from datetime import datetime
import os
# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Define CSV
file_path = "data/live_sales.csv"

# Define CSV
columns = [
    "order_id",
    "order_time",
    "product",
    "category",
    "quantity",
    "price",
    "city",
    "payment_mode"
]

# CSV create with HEADER (VERY IMPORTANT)
if not os.path.exists(file_path):
    pd.DataFrame(columns=columns).to_csv(file_path, index=False)
# Sample data
products = ["Pizza", "Burger", "Pasta", "Sandwich"]
cities = ["Bhopal", "Indore", "Delhi"]
payments = ["Cash", "UPI", "Card"]

# Infinite loop to generate data
while True:
    data = {
        "order_id": random.randint(1000, 9999),
        "order_time": datetime.now(),
        "product": random.choice(products),
        "category": "Food",
        "quantity": random.randint(1, 5),
        "price": random.randint(100, 500),
        "city": random.choice(cities),
        "payment_mode": random.choice(payments)
    }

    pd.DataFrame([data]).to_csv(
        file_path,
        mode="a",
        header=False,   # header sirf pehli baar
        index=False
    )

    print("New order added")
    time.sleep(5) # wait for 5 seconds before adding next order
