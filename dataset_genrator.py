import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

num_users = 500

# Generate user IDs
user_ids = np.arange(1001, 1001 + num_users)

# Age (18–35, mostly students/young users)
ages = np.random.randint(18, 35, num_users)

# SIP amount (₹500 to ₹5000)
sip_amounts = np.random.choice([500, 1000, 1500, 2000, 3000, 5000], num_users)

# Frequency
frequencies = np.random.choice(['Daily', 'Weekly', 'Monthly'], num_users, p=[0.3, 0.5, 0.2])

# Start date (last 6 months)
start_dates = [datetime.today() - timedelta(days=random.randint(30, 180)) for _ in range(num_users)]

# Simulate total investments based on frequency
total_investments = []
last_investment_dates = []
stopped_status = []

for i in range(num_users):
    freq = frequencies[i]
    start = start_dates[i]
    
    if freq == 'Daily':
        interval = 1
    elif freq == 'Weekly':
        interval = 7
    else:
        interval = 30

    max_possible = (datetime.today() - start).days // interval
    
    # Simulate dropout behavior
    if random.random() < 0.4:  # 40% users drop off
        investments = random.randint(1, max(2, int(max_possible * 0.4)))
        stopped = "Yes"
    else:
        investments = max_possible
        stopped = "No"

    last_date = start + timedelta(days=investments * interval)

    total_investments.append(investments)
    last_investment_dates.append(last_date)
    stopped_status.append(stopped)

# Create DataFrame
df = pd.DataFrame({
    'user_id': user_ids,
    'age': ages,
    'sip_amount': sip_amounts,
    'frequency': frequencies,
    'start_date': [d.strftime('%Y-%m-%d') for d in start_dates],
'last_investment_date': [d.strftime('%Y-%m-%d') for d in last_investment_dates],
    'total_investments': total_investments,
    'stopped': stopped_status
})

# Save to CSV
df.to_csv("crypto_sip_dataset.csv", index=False)

print("✅ Dataset generated successfully: crypto_sip_dataset.csv")
print(df.head())