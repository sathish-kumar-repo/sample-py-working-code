import pandas as pd
from datetime import datetime, timedelta

# Generate sample dates (10 days starting from today, descending order)
today = datetime.today()
dates = [today - timedelta(days=i) for i in range(10)]

# Create dummy data for rules (Rule 1 to Rule 10)
rules_data = {
    "Date": dates,
    "Rule 1": [f"Status {i%3}" for i in range(10)],
    "Rule 2": [f"Status {(i+1)%3}" for i in range(10)],
    "Rule 3": [f"Status {(i+2)%3}" for i in range(10)],
    "Rule 4": [f"Status {i%3}" for i in range(10)],
    "Rule 5": [f"Status {(i+1)%3}" for i in range(10)],
    "Rule 6": [f"Status {(i+2)%3}" for i in range(10)],
    "Rule 7": [f"Status {i%3}" for i in range(10)],
    "Rule 8": [f"Status {(i+1)%3}" for i in range(10)],
    "Rule 9": [f"Status {(i+2)%3}" for i in range(10)],
    "Rule 10": [f"Status {i%3}" for i in range(10)],
}

# Create a DataFrame and sort by Date descending
df = pd.DataFrame(rules_data)
df = df.sort_values(by="Date", ascending=False)

# Save to Excel
file_path = "/mnt/data/Rules_Tracking.xlsx"
df.to_excel(file_path, index=False)

file_path
