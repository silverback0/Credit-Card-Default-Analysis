# Credit Card Default Risk Analysis 
### End-to-End Financial Data Pipeline & Business Intelligence

## Project Overview
This project addresses a critical banking problem: **Predicting Credit Risk.** Using a dataset of 30,000 clients, I built a data pipeline that moves raw data from CSV to a PostgreSQL database, performs SQL transformations, and uses Python to visualize high-risk segments.



## Tech Stack
* **Database:** PostgreSQL (Data Modeling & Views)
* **Pipeline:** Python (SQLAlchemy, Pandas)
* **Visualization:** Seaborn, Matplotlib
* **Version Control:** Git & GitHub

## Data Pipeline Workflow
1.  **Ingestion:** Automated the loading of raw CSV data into a local PostgreSQL instance using SQLAlchemy.
2.  **Transformation (SQL):** Created database **Views** to handle data cleaning, renaming columns for business clarity, and mapping numeric codes (e.g., Education: 1) to human-readable labels (e.g., 'Graduate School').
3.  **Analysis:** Performed Exploratory Data Analysis (EDA) using SQL aggregate functions and Python to identify correlation between demographics and default rates.

## Key Business Insights
* **Education Impact:** Customers with a **High School** education showed a significantly higher default rate (~25%) compared to those with **Graduate** degrees.
* **Risk Heatmap:** The combination of being **Single** and having lower education levels represents the highest risk quadrant for the bank.
* **Credit Utilization:** I identified that low credit limits are often associated with higher default frequencies, suggesting a need for stricter vetting for entry-level credit products.

## Project Structure
* `load_to_postgres.py`: Python script for database ingestion.
* `transform_data.sql`: SQL scripts for creating the cleaned analysis views.
* `visualize_risk.py`: Python script generating the risk heatmap.
* `risk_heatmap.png`: Final visualization for executive reporting.

---
