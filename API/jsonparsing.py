import json
data='{"id": "123456","title": "The Great Gatsby","genre": ["Fiction", "Classic"]}'
data_dict=json.loads(data)

print(type(data_dict))
print(data_dict['genre'][0])