import csv
import random

def generate_age():
    return random.randint(18, 65)

def generate_income():
    return random.randint(20, 100)  # Multiples of $1000

def generate_owns_house():
    return random.choice(['Yes', 'No'])

def generate_previous_default():
    return random.choice(['Yes', 'No'])

def decide_approval(age, income, owns_house, prev_default):
    if prev_default == "Yes":
        return 'No'
    if income < 30:
        return 'No'
    if owns_house == "Yes" and income > 50:
        return 'Yes'
    if age > 40 and income > 40:
        return 'Yes'
    return random.choice(['Yes', 'No'])

# Generate dataset
data = []

# Adding header
data.append(["Applicant ID", "Age", "Income ($1000s)", "Owns House", "Previous Default", "Approved"])

for i in range(1000):
    age = generate_age()
    income = generate_income()
    owns_house = generate_owns_house()
    prev_default = generate_previous_default()
    approved = decide_approval(age, income, owns_house, prev_default)
    
    data.append([i+1, age, income, owns_house, prev_default, approved])

# Write to CSV
with open('loan_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Dataset 'loan_data.csv' generated!")
