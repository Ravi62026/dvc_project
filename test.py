import pandas as pd

data = [
    {"name": "John", "age": 25, "city": "New York"},
    {"name": "Alice", "age": 30, "city": "Los Angeles"},
    {"name": "Bob", "age": 35, "city": "Chicago"},
    {"name": "Eve", "age": 20, "city": "New York"},
    {"name": "Mike", "age": 40, "city": "Los Angeles"},
]

df = pd.DataFrame(data)

df.to_csv("data/data.csv", index=False)