import json

with open('input_7.json', 'r') as file:
    data = json.load(file)

filtered = []
for i in data:
    if i['age'] > 25:
        filtered.append(i)

with open('output_7.json', 'w') as file:
    json.dump(filtered, file, indent=1)
