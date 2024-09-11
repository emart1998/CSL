import pandas as pd
import random

# Define the data
team_members = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
states = ['IL', 'CA', 'NY', 'TX', 'FL','NY','PA','OH','CA','CT','GA']
genders = ['Male', 'Female']
reasons = {
    '1': 'Terrible service',
    '2': 'Claim Was Denied',
    '3': 'Bad service',
    '4': 'Poor service',
    '5': 'Average service',
    '6': 'Good service',
    '7': 'Very good service',
    '8': 'No Returned Calls',
    '9': 'Excellent service',
    '10': 'Outstanding service'
    }

# Generate the data
data = []
for member in team_members:
    for i in range(500):
        claim_number = f'CLM{random.randint(1000, 9999)}'
        state = random.choice(states)
        customer_name = f'Customer{random.randint(1, 100)}'
        gender = random.choice(genders)
        score = random.randint(1, 10)
        reason = reasons[str(score)]
        data.append([member, claim_number, state, customer_name, gender, score, reason])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Team Member', 'Claim Number', 'State', 'Customer Name', 'Gender', 'Survey Score', 'Reason for Score'])

# Save to Excel
df.to_excel('sample_data.xlsx', index=False)