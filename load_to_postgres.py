import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

db_password = os.getenv('DB_PASSWORD')
df= pd.read_csv('UCI_Credit_Card.csv')

engine = create_engine(f'postgresql://postgres:{db_password}@localhost:5432/credit_db')

try:
    df.to_sql('credit_card_data', engine, if_exists='replace', index=False)
    print("Data loaded successfully to PostgreSQL.")
except Exception as e:
    print(f"An error occurred: {e}")