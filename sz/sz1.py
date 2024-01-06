import random
'''num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)'''


'''num3 = int(input('Введите число меньше 20: '))
if num3>=20:
    print('Too high')
else:
    print('Thank you')'''

'''num4 = int(input('Введите число от 10 до 20(включительно): '))
if num4>=10 and num4<=20:
    print('Thank you')
else:
    print('Incorrect answer')'''

'''text1 = input('Введите любимый цвет ')
if text1=='red' or text1=='RED' or text1=='Red':
    print('I like red too')
else:
    print(f"I don't like {text1}, I prefer red")'''

'''text2 = str.lower(input('Идёт ли дождь? '))
if text2 == 'yes':
    text3 = str.lower(input('На улице ветренно? '))
    if text3 == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')'''

'''text4 = int(input('Введите свой возраст: '))
if text4 >= 18:
    print('You can vote')
elif text4 == 17:
    print('You can learn to drive')
elif text4 == 16:
    print('You can buy a lottery ticket')
elif text4 < 16:
    print('You can go Trickor-Treating')
else:
    print('Incorect answer')'''

'''num5 = int(input('Введите число: '))
if num5 < 10:
    print('Too low')
elif num5 >= 10 and num5 <= 20:
    print('Correct')
else:
    print('Too high')'''

'''num6 = input('Введите значение 1,2 или 3 ')
if int(num6) == 1:
    print('Thank you')
elif int(num6) == 2:
    print('Well done')
elif int(num6) == 3:
    print('Correct')
else:
    print('Error message')
'''

'''text = "  This is some text.  "
print(text.strip(" "))'''

'''name = input('Введите имя ')
print(len(name))'''

'''name1 = input('Введите имя ')
name2 = input('Введите фамилию ')
a = ' '
name3 = name1 + a + name2
print(name3)
print(len(name3))'''

'''name1 = input('Введите имя ')
name2 = input('Введите фамилию ')
name3 = name1.title() + name2.title()
print(name3)'''

'''text1 = input('Введите предложение ')
a = int(input('Начало '))
b = int(input('конец '))
print(text1[a:b])
'''

'''name1 = input('Введите имя ')
if len(name1) <= 5:
    name2 = input('Введите фамилию ')
    print(name1.upper() + name2.upper())
else:
    print(name1.lower())'''
import math
'''#27-28
num5 = float(input('Введите число'))
num6 = num5*2
print(num6)
print(round(num6, 2))'''
#29
'''num7 = int(input('Введите число больше 500 '))
num8 = math.sqrt(num7)
print(round(num8, 2))'''
#30
#print(round(math.pi, 5))

#31
'''num9 = int(input('Введите радиус круга '))
s = math.pi * (num9**2)
print(s)'''

#32
'''r = int(input('Введите радиус цилинтра '))
h = int(input('введите высоту цилинтра '))
v = (math.pi * (r**2)) * h
print(round(v, 3))'''

#33
'''n1 = int(input('Введите число 1 '))
n2 = int(input('Введите число 2 '))
n3 = n1 // n2
n4 = n1 % n2
print(f'если разделишь {n1} на {n2}, получится {n3} с остатком {n4}')'''

#34
'''b = int(input('1) Square \n2) Triangle \nEnter a number: '))
if b == 1:
    c = int(input('Введите длину стороны квадрата '))
    s = c**c
    print(s)
elif b == 2:
    d = int(input('Введите длину стороны треугольника '))
    e = int(input('Введите высоту треугольника '))
    s2 = 0.5 * d * e
    print(s2)
else:
    print('Input error')'''
#35-36
'''name = input('Введите имя ')
k = int(input('Введите число '))
for i in range(k):
    print(name)'''
#37-38
'''name = input('Введите имя ')
k = int(input('Введите число '))
for i in range(k):
    for j in name:
        print(j)'''
#39
'''w = int(input('Введите число от 1 до 12 '))
for i in range(1, 13):
    r = w * i
    print(f'{w}*{i}={r}')'''
#40
'''f = int(input('Введите число до 50 '))
for i in range(f, 0, -1):
    print(i)'''
#41
'''name = input('Введите имя ')
num = int(input('Введите число '))
if num < 10:
    for i in range(num):
        print(name)
else:
    for i in range(3):
        print('Too high')'''
#42
'''total = 0
for i in range(2):
    n1 = int(input('число '))
    e = input('Включить в total? ')
    if e == 'да':
        total = total + n1
print(total)'''
#43
'''y = input('В каком направлении вести отсчёт (в прямом 0, в обратном 1) ')
if y == '0':
    num1 = int(input('Введите число '))
    for i in range(1, num1+1):
        print(i)
elif y == '1':
    num2 = int(input('Введите число меньше 20 '))
    for i in range(20, num2+1, -1):
        print(i)
else:
    print('I don’t understand')'''
#44
'''people = int(input('Сколько человек хотим пригласить '))
if people < 10:
    for i in range(0, people):
        name = input('Введите имя гостя ')
        print(f'{name} has been invited')
else:
    print('Too many people')'''
#45
'''total = 0
while total <= 50:
    total = total + int(input('Ваедите число '))
    print('The total is ', total)'''

#46
'''num = 4
while num >= 5:
    num = int(input('Введите число '))
    print('The last number you entered was a', num)'''

#47
'''summ = int(input('Введите число '))
text = 'y'
while text != 'n':
    num2 = int(input('Введите число '))
    summ += num2
    text = input('Продолжить? ')
print(summ)
'''
#48
'''w = 'y'
c = 0
while w != 'n':
    name = input('Введите имя ')
    c += 1
    w = input('Хотите пригласить кого-то ещё? ')
print(c)'''

#49
'''compnum = 50
n = 0
c = 0
while n != compnum:
    n = int(input('Input number '))
    if n < compnum:
        print('Input number < compnum')
    elif n > compnum:
        print('Input number > compnum')
    c += 1
print(f'Well done, you took {c} attempts')'''
#50
'''n = 0
while n <= 10 or n >= 20:
    n = int(input('введите число от 10 до 20 '))
    if n < 10:
        print('Too low')
    if n > 20:
        print('Too high')
print('Thank you')'''
#51
'''num = 10
print(f'There are {num} green bottles hanging on the wall, {num} green bottles hanging on the wall, and if 1 green bottle should accidentally fall')
while num != 0:
    n = int(input('how many green bottles will be hanging on the wall? '))
    num -= 1
    if n == num:
        print(f'There will be {num} green bottles hanging on the wall')
    else:
        print('No, try again')
print('There are no more green bottles hanging on the wall')'''

# num = random.randint(0, 9)
# num = random.randrange(0, 100, 5)
# colour = random.choice(["red", "black", "green"])

#52
#print(random.randint(0, 100))

#53
#print(random.choice(["яблоко", "банан", "апельсин", "мандарин", "ананас"]))

#54
'''r = random.choice(['h', 't'])
u = input('Угадайте значение (h/t) ')
if u == r:
    print('You win')
else:
    print('Bad luck')
print(f'было {r}')'''

#55
'''n = random.randint(1, 5)
t = int(input('Выберите число '))
if t == n:
    print('Well done')
elif t > n:
        t = int(input('Ваше число больше, ещё раз '))
        if t == n:
            print('Correct')
        else:
            print('You lose')
elif t < n:
        t = int(input('Ваше число меньше, ещё раз '))
        if t == n:
            print('Correct')
        else:
            print('You lose')'''


