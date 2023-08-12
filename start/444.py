'''list1 = [1, 2, 3, 4]
list2 = [5, 6, 7]
list3 = [list1, list2]

print(list3)
print(id(list3))'''

'''some_tuple = (1, 2, 3)
print(some_tuple)
temp = list(some_tuple)
temp[0] = 100
some_tuple = tuple(temp)
print(some_tuple)
'''

'''print(user['username'])
print(user['password'])

user['username'] = 'Admin'
print(user['username'])
'''
'''user = {
    'username':'admin',
    'password': 54321
}

for key in user:
    print(user[key])'''

emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
          'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
          'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
          'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
          'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
          'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
for i in emails:
    for j in emails[i]:
        print(f'{j}@{i}')
