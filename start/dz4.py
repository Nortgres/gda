'''Напишите функцию find_or_add которая принимает в себя 3 параметра словарь,ключ, и значение которое по умолчанию равно None.
Если в словаре есть значение по переданному ключу, то возвращается значение. Если такого ключа в словаре нет,
то в словаре нужно создать элемент с таким ключом и значением переданным при вызове функции и вернуть весь словарь'''

test_dict = {
    'login': 'admin',
    'password': 'qwerty'
}
def find_or_add(test_dict, key, n=None):
    if key in test_dict:
        return test_dict[key]
    else:
        test_dict[key] = n
        return (test_dict)

print(test_dict)
print(find_or_add(test_dict, 'login'))  # должно вывести admin
print(find_or_add(test_dict, 'email', 'test@mail.ru'))  # должно вывести словарь с добавленным "email":"test@mail.ru"
