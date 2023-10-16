'''age = int(input('Введите возраст: '))
if age >= 18:
    print('Продажа алоголя разрешена.')
else:
    print('Продажа алкоголя запрещена.')


gender = input('Введите пол (М/Ж): ')
greeting = 'Привет сестренка!' if gender.upper() == 'Ж' else 'Привет братишка!'
print(greeting)


list1 = list(map(float, input('Введите два числа через пробел: ').split()))
if list1[0] > list1[1]:
    print(list1[0])
else:
    print(list1[1])


# Задание 5.2.
c = input('Введите слово: ').upper()
if c[::-1] == c:
    print('Palindrome')
else:
    print('Not a Palindrome')

# Задание 5.3.
list2 = list(map(int, input('Введите два числа через пробел: ').split()))
if list2[0] % list2[1] ==0:
    print(list2[0] // list2[1])
else:
    print(f'{list2[0]} на {list2[1]} нацело не делится')

# Задание 5.4.
a, b, c = map(int, input('Введите три числа через пробел: ').split())
if (a**2 + b**2) != c**2:
    print('No')
else:
    print('Yes')

# Задание 5.5.
num = int(input('Введите пятизначное число: ')[-1])
print('Yes') if num == 7 else print('No')

# Задание 5.6.
word = input('Введите слово: ').lower()
print('Yes') if 't' in word and 'h' in word and 'o' in word else print('No')
'''
