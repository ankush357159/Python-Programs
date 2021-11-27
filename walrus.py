sample_data = [
    {"userId": 1, "name": "rahul", "completed": False},
    {"userId": 1, "name": "rohit", "completed": False},
    {"userId": 1, "name": "ram", "completed": False},
    {"userId": 1, "name": "ravan", "completed": True},
]

for entry in sample_data:
    if name := entry.get("name"):
        print(f'Found name: "{name}"')

for entry in sample_data:
    name = entry.get("name")
    if name:
        print(f'Found name: "{name}" ')

