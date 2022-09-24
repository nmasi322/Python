# JSON is commonly used with data APIs. How can we parse JSON into a Python dictionary????
import json

# somple json
user_json = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# parse to dict
user = json.loads(user_json)  # similar to JSON.parse in JS
print(user)
