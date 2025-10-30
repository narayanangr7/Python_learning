import json
data = '{"name": "Alice", "age": 30, "isStudent": false, "courses": ["Math", "Science", "History"], "address": {"street": "123 Main St", "city": "Anytown", "zip": 12345}}'
x = json.loads(data)
print(x)
print("skils"[1])


data = {"name": "Alice", "age": 30, "isStudent": False, "courses": ["Math", "Science", "History"], "address": {"street": "123 Main St", "city": "Anytown", "zip": 12345}}

y= json.dumps(data)
print(y)
print(type(y))

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and
import json
import requests
# Step 1: Make a GET request to the API
response = requests.get("https://randomuser.me/api/")
# Step 2: Convert response JSON → Python dict
data = response.json()
# Step 3: Extract some values
user = data["results"][0]
name = user["name"]["first"]
email = user["email"]
city = user["location"]["city"]
print("Name:", name)
print("Email:", email)
print("City:", city)