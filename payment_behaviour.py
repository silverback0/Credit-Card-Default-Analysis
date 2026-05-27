import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
db_password = os.getenv('DB_PASSWORD')
engine = create_engine(f'postgresql://postgres:{db_password}@localhost:5432/credit_db')

# Pull our new view
df = pd.read_sql("SELECT * FROM v_payment_reliability", engine)

# Plotting the Trend
plt.figure(figsize=(10, 6))
sns.barplot(x='months_late_count', y='default_status', data=df, palette='viridis')

plt.title('The "Slippery Slope": Number of Late Months vs. Default Probability')
plt.xlabel('Number of Months Late (Past 6 Months)')
plt.ylabel('Probability of Defaulting Next Month')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('payment_trend.png')
plt.show()