import csv

users = [
    ['username', 'password', 'is_admin']
]

with open('users.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(users)
    writer.writerows(['username2', 'password2', 'is_admin2'])

