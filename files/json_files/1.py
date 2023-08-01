import json

class MyEncoder(json.JSONEncoder):

'''    def default(self, o):
        if isinstance(o, set):
            return list(o)'''

#json.encoder()

message = {
    'from': 'vlad',
    'to': 'anton',
    'text': 'Hi!',
    'on_delte': None,
    'tuple': (1, 2, 3),
    'number': 5,
    'bool': True
}

json_str = json.dumps(message)
print(json_str)
decoded = json.loads(json_str)
print(decoded)

with open('message.json') as f:
    data = j