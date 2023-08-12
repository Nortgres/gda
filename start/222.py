

'''password = 'key'
a = (input('Введите пароль '))
while a != password:
    a = input('пароль не верный. Введите пароль ')
print('пароль верный')
'''

password = 'key'
while True:
    user_pass = input('Введите пароль')
    if user_pass == password:
        print('Пароль верный')
        break
