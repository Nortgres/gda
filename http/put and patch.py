import requests

data = {
    "title": "ttest2"
}
res = requests.put(url='https://jsonplaceholder.typicode.com/posts/1', data=data) #полное обнвовление
res2 = requests.patch(url='https://jsonplaceholder.typicode.com/posts/1', data=data) #полное обнвовление

print(res.json())
print(res2.json())