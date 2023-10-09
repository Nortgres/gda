'''
# задание 3.1
list1 = input('').split()
list1 = list(map(int, list1))
print(list1)

# задание 3.2
list2 = input('Введите названия городов через пробел: ').split()
city = input('Введите название искомого города: ')
print(city in list2)

# задание 3.3
list3 = input('Введите названия городов через пробел: ').split()
print(list3[-1])

# задание 3.4
list4 = input('Введите оценки студентов через пробел: ').split()
list4 = list(map(int, list4))
n = sum(list4)/len(list4)
print(round(n,1))

# задание 3.5
list5 = input('Вводится число новых подписчиков канала по дням в одну строку через пробел: ').split()
list5 = list(map(int, list5))
print(f'{max(list5)} {min(list5)} {sum(list5)}')

# задание 3.6
list6 = input('В одну строчку через пробел введите: имя, отчество и фамилия: ').split()
print(f'{list6[2]} {(list6[0])[0]}. {(list6[1])[0]}.')

# задание 3.7
list7 = ["Москва", "Тверь", "Вологда"]
list7.extend(input('Введите названия городов через пробел: ').split())
print(*list7)

# задание 3.8
list8 = ["Москва", "Тверь", "Вологда"]
list9 = input('Введите названия городов через пробел: ').split()
list10 = list9 + list8
print(*list10)

# задание 3.9
list11 = input('Вводятся числа просмотров видео по дням (целые числа) в одну строку через пробел: ').split()
list11 = list(map(int, list11))
print(list11[0:3])

# задание 3.10
list12 = input('Вводятся числа просмотров видео по дням (целые числа) в одну строку через пробел: ').split()
list12 = list(map(int, list12))
print(list12[-4:])

# задание 3.11
list13 = input('Введите названия городов через пробел: ').split()
print(list13[::2])

#задание 3.12
list14 = input('Введите названия городов через пробел: ').split()
print(list14[1::2])

#задание 3.13
list15 = input('Введите оценки студентов через пробел: ').split()
list15 = list(map(int, list15))
print(list(reversed(list15[2:7])))

#задание 3.14 ???
list16 = input('Введите оценки студентов через пробел: ').split()
list16 = list(map(int, list16))
print(list(reversed(list16[::-2])))


#задание 3.15
list17 = input('Введите строку из целых чисел через пробел: ').split()
list17 = list(map(int, list17))
list17.append(list17[0]!=list17[-1])
print(*list17)

#задание 3.16
list18 = input('Введите названия городов через пробел: ').split()
newcity = input('Введите название нового города')
list18.insert(1, newcity)
print(*list18)

#задание 3.17
n_book = input('Введите название книги: ')
a_book = input('Введите автора книги: ')
s_book = int(input('Введите число страниц: '))
p_book = float(input('Введите цену: '))
l_book = [n_book, a_book, s_book, p_book]
l_book.remove(s_book)
l_book[1] = 'Пушкин'
l_book[2] = p_book*2
print(l_book)

#задание 3.18
list19 = list(map(int, input('Вводится число новых подписчиков канала по дням в одну строку через пробел: ').split()))
print(*(sorted(list19, reverse=True)))

#задание 3.19
list20 = list(input('Введите номер телефона: '))
del list20[0:2], list20[8], list20[10]
list20.insert(0,8)
print(''.join(map(str, list20)))

#задание 3.20
list21 = list(map(int, input('Введите строку из целых чисел через пробел: ').split()))
list21.sort()
print(list21[0], list21[1], list21[2])

#задание 3.21
list22 = list(map(int, input('Введите строку из целых чисел через пробел: ').split()))
x = list22.pop(-1)
list22.append(x % 2 !=0)
print(*list22)

#задание 3.22
list23 = list(map(int, input('Вводятся оценки студента (целые числа) в одну строку через пробел: ').split()))
print(list23.count(2))

#задание 3.23
list24 = input('Введите названия рек: ').split()
list24.sort()
list24.pop(0)
print(*list24)

#задание 3.24
list25 = list(map(float, input('Введите строку из числел с плавающей точкой через пробел: ').split()))
list26 = list(map(int, input('Введите строку из целых чисел через пробел: ').split()))
list25.append(list26)
print(list25)

#задание 3.25
str1 = input('Введите первую строку: ').split()
str2 = input('Введите вторую строку: ').split()
str3 = input('Введите третью строку: ').split()
list27 = [str1, str2, str3]
print(list27)

#задание 3.26
num1 = list(map(int, input('Введите числа первой строки: ').split()))
num2 = list(map(int, input('Введите числа второй строки: ').split()))
num3 = list(map(int, input('Введите числа третьей строки: ').split()))
list28 = [num1[-1], num2[-1], num3[-1]]
print(*list28)

#задание 3.27
list29 = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
          ["Москва", "спаленная", "пожаром"],
          ["Французу", "отдана?"]]
word = input('Введите слово: ')
#data = []
#for i in list29:
#    for j in i:
#        data.append(j)
#print(word in data)
condition = word in list29[0] or \
            word in list29[1] or \
            word in list29[2]
print(condition)
'''
