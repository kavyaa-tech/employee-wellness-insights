import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Simulate 10,000 employee checkups
n = 10000
data = pd.DataFrame({
    'employee_id': [fake.uuid4() for _ in range(n)],
    'date': pd.to_datetime(np.random.choice(pd.date_range("2022-01-01", "2023-12-31"), n)),
    'age': np.random.randint(22, 65, size=n),
    'gender': np.random.choice(['Male', 'Female', 'Other'], size=n),
    'company': np.random.choice(['TCS', 'Infosys', 'Accenture', 'Wipro', 'TechM'], size=n),
    'location': np.random.choice(['Mumbai', 'Bangalore', 'Hyderabad', 'Delhi', 'Pune'], size=n),
    'blood_pressure': np.random.randint(90, 180, size=n),
    'sugar_level': np.random.randint(60, 250, size=n),
    'cholesterol': np.random.randint(120, 300, size=n)
})
df = pd.read_csv("D:/health_checkup_data.csv")
