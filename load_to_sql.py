import pandas as pd
import time
from sqlalchemy import create_engine

# MySQL connection (password blank because workbench login ho raha hai)
engine = create_engine(
    "mysql+pymysql://root:Mysql%402002@localhost:3306/realtime_db"
)

# Infinite loop to load data

while True:
    try:
        df = pd.read_csv("data/live_sales.csv")

        df.to_sql(
            "sales_data",
            engine,
            if_exists="append",   # IMPORTANT: append, replace nahi
            index=False
        )

        print("Data inserted into MySQL")
        time.sleep(10)

    except Exception as e:
        print("Error:", e)
        time.sleep(10)
