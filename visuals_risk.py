import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import load_dotenv

# 1. Connect to your database
load_dotenv()
db_password = os.getenv('DB_PASSWORD')
engine = create_engine(f'postgresql://postgres:{db_password}@localhost:5432/credit_db')

# 2. Pull the aggregated data (using the same logic you just tested in SQL!)
query = """
SELECT 
    education_level,
    marital_status,
    ROUND(AVG(default_payment_next_month)::numeric * 100, 2) AS default_rate
FROM v_cleaned_credit_analysis
GROUP BY education_level, marital_status
"""
df = pd.read_sql(query, engine)

# 3. Pivot the data for a Heatmap
# This turns your rows into a grid
pivot_table = df.pivot(index='education_level', columns='marital_status', values='default_rate')

# 4. Create the Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table, annot=True, cmap='RdYlGn_r', fmt='.1f')

plt.title('Default Risk Heatmap (%) \n (Red = Higher Risk, Green = Lower Risk)')
plt.tight_layout()

# 5. Save it for your GitHub
plt.savefig('risk_heatmap.png')
plt.show()