import json

# Serialize a dictionary
dict = {'name': 'Sankalpa Pokhrel', 'age': 22}
with open("data.json", "w") as write_file:
    json.dump(dict, write_file)

# Deserialize the JSON back into Python
with open("data.json", "r") as read_file:
    data = json.load(read_file)
print(data)