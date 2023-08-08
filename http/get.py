import requests


res = requests.get('https://jsonplaceholder.typicode.com/posts')
#print(requests.get('https://jsonplaceholder.typicode.com/posts').json()[0:5])
print(res.json()[0:5])
