import pandas as pd

data = [
    {"name": "ravi", "age": 20, "city": "New York"},
    {"name": "raunak", "age": 30, "city": "Los Angeles"},
    {"name": "kiran", "age": 35, "city": "Chicago"},
    {"name": "shankar", "age": 20, "city": "New York"},
    {"name": "dadi", "age": 40, "city": "Los Angeles"},
]

df = pd.DataFrame(data)

df.to_csv("data/data.csv", index=False)