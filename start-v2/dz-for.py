'''
Задание 6.1. Вводятся два целых положительных числа n и m, причем, n < m. Вывести в
строку через пробел квадраты целых чисел в диапазоне [n; m]. Программу реализовать при
помощи цикла while.
Пример ввода:
2 4
Пример вывода:
4 9 16
''' '''
# Задание 6.1.
n, m = map(int, input('Введите два положительных числа: ').split(' '))
list1 = []
if n < m:
    while n <= m:
        list1.append(n**2)
        n = n + 1
    print(*list1)
else:
    print('Первое число должно быть меньше второго.')
''' '''
Задание 6.2. Вводится стоимость одной книги (вещественное число). Необходимо вывести
на экран в строчку через пробел стоимости 2, 3, ... 10 таких книг с точностью до десятых.
Программу реализовать при помощи цикла while.
Пример ввода:
34.6
Пример вывода:
69.2 103.8 138.4 173.0 207.6 242.2 276.8 311.4 346.0
''' '''
# Задание 6.2.
price = float(input('Введите стоимость книги: '))
list2 = []
x = 1
while x < 11:
    list2.append(round(price*x, 1))
    x += 1
print(*list2)
''' '''
Задание 6.3. Вводится целое положительное число n. Вычислить и вывести на экран сумму:
1 + 1/2 + 1/3 + ... + 1/n с точностью до тысячных (три знака после запятой). Программу
реализовать при помощи цикла while.
Пример ввода:
8
Пример вывода:
2.718
''' '''
# Задание 6.3.
n = int(input('Введите целое положительное число: '))
x = 1
s = 0
while x <= n:
    s += 1 / x
    x += 1
print(round(s, 3))
''' '''
Задание 6.4. На каждой итерации цикла пользователь вводит целое число. Цикл
продолжается, пока не встретится число 0. Необходимо вычислить сумму введенных в
цикле чисел и вывести результат на экран. Программу реализовать при помощи цикла while.
Пример ввода:
8
11
2 -4 0
Пример вывода:
17
''' '''
# Задание 6.4.
n1 = 1
s1 = 0
while n1 != 0:
    n1 = int(input('Введите целое число: '))
    s1 += n1
print(s1)
''' '''
Задание 6.5. Вводится строка. Замените в этой строке все подряд идущие дефисы
(--, ---, ---- и т.д.) на одинарные (-). Результат преобразования строки выведите на экран.
Программу реализовать при помощи цикла while.
Пример ввода:
osnovnye--metody-----slovarey
Пример вывода:
osnovnye-metody-slovarey
''' '''
# Задание 6.5.
str = input('Введите строку: ')
newstr = ''
k = 0
while k < len(str):
    if str[k] == '-':
        c = 1
        while k + c < len(str) and str[k + c] == '-':
            c += 1
        newstr += '-'
        k += c
    else:
        newstr += str[k]
        k += 1
print(newstr)
''' '''
Задание 6.6. Вводится натуральное (то есть, целое положительное) число (от трехзначного
и более). Найти произведение всех его цифр. Результат вывести на экран. Программу
реализовать при помощи цикла while.
Пример ввода:
821
Пример вывода:
16
''' '''
# Задание 6.6.
num = int(input("Введите натуральное число: "))
key = 1
while num > 0:
    a = num % 10
    key *= a
    num //= 10

print(key)
''' '''
Задание 6.7. Последовательность Фибоначчи образуется так: первые два числа равны 1 и
1, а каждое последующее число равно сумме двух предыдущих. Имеем такую
последовательность чисел: 1, 1, 2, 3, 5, 8, 13, ... Постройте последовательность Фибоначчи
длиной n (n вводится с клавиатуры). Результат отобразите в виде строки полученных чисел,
записанных через пробел. Программу реализовать при помощи цикла while.
Пример ввода:
8
Пример вывода:
1 1 2 3 5 8 13 21
''' '''
# Задание 6.7.
n = int(input('Введите число: '))
i = 1
rez = [1, 1]
while len(rez) < n:
    x = rez[-1] + rez[-2]
    rez.append(x)
    i += 1
print(*rez)
''' '''
Задание 6.8. Одноклеточная амеба каждые 3 часа делится на 2 клетки. Определить,
сколько клеток будет через n часов (n - целое положительное число, вводимое с
клавиатуры). Считать, что изначально была одна амеба. Результат вывести на экран.
Задачу необходимо решить с использованием цикла while.
Пример ввода:
11
Пример вывода:
8
''' '''
# Задание 6.8.
n = int(input('Введите колличество часов: '))
a = 1
i = 1
while i <= n:
    if i%3 == 0:
        a *= 2
        i += 1
    else:
        i += 1
print(a)
''' '''
Задание 6.9. Гражданин 1 января открыл счет в банке, вложив 1000 руб. Каждый год размер
вклада увеличивается на 5% от имеющейся суммы. Определить сумму вклада через n лет
(n - целое положительное число, вводимое с клавиатуры). Результат округлить до сотых и
вывести на экран. Программу реализовать при помощи цикла while.
Пример ввода:
5
Пример вывода:
1276.28
''' '''
n = int(input('Введите колличество лет: '))
s = 1000
i = 1
while i <= n:
    s *= 1.05
    i += 1
print(round(s, 2))
''' '''
Задание 6.10. Вводятся два натуральных четных числа n и m в одну строчку через пробел,
причем n < m. Напечатать все нечетные числа из интервала [n, m]. Задачу решить без
применения условного оператора. Результат вывести на экран в виде строки чисел,
записанных через пробел. Программу реализовать при помощи цикла while.
Пример ввода:
2 10
Пример вывода:
3 5 7 9
''' '''
n, m = map(int, input('Введите два числа через пробел: ').split())
l1 = []
while n < m:
    if n % 2 != 0:
        l1.append(n)
        n += 1
    else:
        n += 1
print(*l1)
''' '''
Задание 6.11. Составить программу поиска всех трехзначных чисел, которые при делении
на 47 дают в остатке 43 и кратны 3. Вывести найденные числа в строчку через пробел.
Программу реализовать при помощи цикла while.
Пример ввода:
Пример вывода:
231 372 513 654 795 936
''' '''
l2 = []
n = 100
while n < 1000:
    if n % 47 == 43 and n % 3 == 0:
        l2.append(n)
        n += 1
    else:
        n += 1
print(*l2)
''' '''
Задание 6.12. Имеется одномерный список длиной 10 элементов, состоящий из нулей. На
каждой итерации цикла пользователь вводит целое число - индекс элемента списка p, по
которому записывается значение 1, если ее там еще нет. Если же 1 уже проставлена, то
список не менять и снова запросить у пользователя очередное число. Необходимо
расставить так пять единиц в список. (После этого цикл прерывается). Программу
реализовать с помощью цикла while и с использованием оператора continue, когда 1 не
может быть добавлена в список. Результат вывести на экран в виде последовательности
чисел, записанных через пробел.
Пример ввода:       Пример вывода:
1 2 2 5 7 5 9       0 1 1 0 0 1 0 1 0 1
''' '''
p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while i < 5:
    x = int(input('Введите число: '))
    if p[x] == 1:
        continue
    p[x] = 1
    i += 1
print(*p)
''' '''
Задание 6.13. На каждой итерации цикла вводится целое число. Необходимо подсчитать
произведение только положительных чисел, до тех пор, пока не будет введено значение 0.
Реализовать пропуск вычислений с помощью оператора continue, а также использовать
цикл while. Результат произведения вывести на экран.
''' '''
n = 1
x = 1
while True:
    n = int(input('Введите целое число: '))
    if n > 0:
        x *= n
    elif n == 0:
        break
    else:
        continue
print(x)
''' '''
Задание 6.14. Вводится список названий городов в одну строчку через пробел. Определить,
что в этом списке все города имеют длину более 5 символов. Реализовать программу с
использованием цикла while и оператора break. Вывести Yes, если условие выполняется и
No - в противном случае.
Пример ввода:
Самара Ульяновск Новгород Воронеж
Пример вывода:
Yes
''' '''
city = list(input('Введите список городов через пробел: ').split())
i = 0
while i < len(city):
    if len(city[i]) <= 5:
        print('No')
        break
    i += 1
else:
    print('Yes')
''' '''
Задание 6.15. Вводится список имен студентов в одну строчку через пробел. Определить,
что хотя бы одно имя в этом списке начинается и заканчивается на ту же самую букву (без
учета регистра). Реализовать программу с использованием цикла while и оператора break.
Вывести Yes, если условие выполняется и No - в противном случае.
Пример ввода:
Петр Анна Иван Сергей Михаил Федор
Пример вывода:
Yes
''' '''
st = list((input('Введите список имен студентов: ').lower()).split())
i = 0
while i < len(st):
    name = st[i]
    if name[0] == name[-1]:
        print('Yes')
        break
    i += 1
else:
    print('No')
''' '''
Задание 6.16. Вводится натуральное число n (то есть, целое положительное). В цикле
перебрать все целые числа в интервале [1; n] и сформировать список из чисел, кратных 3 и
5 одновременно. Вывести полученную последовательность чисел в виде строки через
пробел, если значение n меньше 100. Иначе вывести на экран сообщение "слишком
большое значение n" (без кавычек). Использовать в программе оператор else после цикла
while.
Пример ввода 1:       Пример ввода 2:
49                    100
Пример вывода 1:      Пример вывода 2:
15 30 45              слишком большое значение n
''' '''
n = int(input('Введите натуральное число: '))
if n < 100:
    l4 = []
    i = 0
    while i < n:
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            l4.append(i)
        else:
            continue
    print(*l4)
else:
    print('слишком большое значение n')
''' '''
Задание 6.17. Вводится натуральное число n. Вывести первое найденное натуральное
число (то есть, перебирать числа, начиная с 1), квадрат которого больше значения n.
Реализовать программу с использованием цикла while.
Пример ввода:
10
Пример вывода:
4
''' '''
n = int(input('Введите натуральное число: '))
i = 1
while i*i <= n:
    i += 1
print(i)
''' '''
Задание 6.18. (На использование цикла while). Начав тренировки, лыжник в первый день
пробежал 10 км. Каждый следующий день он увеличивал пробег на 10 % от пробега
предыдущего дня. Определить в какой день он пробежит больше x км (натуральное число x
вводится с клавиатуры). Результат (искомый день) вывести на экран.
Пример ввода:
20
Пример вывода:
9
''' '''
x = int(input('Введите колличество км: '))
d = 10
i = 1
while d < x:
    d += d*0.1
    i += 1
print(i)
''' '''
Задание 6.19. (На использование цикла while). Вводятся названия книг (каждое с новой
строки). Удалить из введенного списка все названия, состоящие из двух и более слов (слова
в названиях разделяются пробелом). Результат вывести на экран в виде строки из
оставшихся названий через пробел.
Пример ввода:
Муму
Евгений Онегин
Сияние
Мастер и Маргарита
Пиковая дама
Колобок
Пример вывода:
Муму Сияние Колобок
''' '''
l_book = []
while True:
    book = input('Вводятся названия книг (каждое с новой строки, для завершения введите stop): ')
    if book != 'stop':
        if ' ' not in book:
            l_book.append(book)
    else:
        break
print(*l_book)

Задание 6.20. С помощью функции range() сформируйте следующую последовательность
чисел: 0, 1, 2, ..., 10
Результат выведите в виде последовательности чисел, записанных через пробел в одну
строчку.
Пример ввода:
Пример вывода:
0 1 2 3 4 5 6 7 8 9 10
''' '''
for i in range(11):
    print(i, end=' ')
''' '''
Задание 6.21. С помощью функции range() сформируйте следующую последовательность
чисел: 10, 9, 8, ..., 0
Результат выведите в виде последовательности чисел, записанных через пробел в одну
строчку.
Пример ввода:
Пример вывода:
10 9 8 7 6 5 4 3 2 1 0
''' '''
for i in range(10, -1, -1):
    print(i, end=' ')
''' '''
Задание 6.22. С помощью функции range() сформируйте следующую последовательность
чисел: -10, -8, -6, -4, -2
Результат выведите в виде последовательности чисел, записанных через пробел в одну
строчку.
Пример ввода:
Пример вывода:
-10 -8 -6 -4 -2
''' '''
num = list(range(-10, -1, 2))
print(*num)
''' '''
Задание 6.23. С помощью функции range() сформируйте следующую последовательность
чисел: 1, 4, 7, 10, 13, 16, 19
Результат выведите в виде последовательности чисел, записанных через пробел в одну
строчку.
Пример ввода:
Пример вывода:
1 4 7 10 13 16 19
''' '''
num = list(range(1, 20, 3))
print(*num)
''' '''
Задание 6.24. Вводятся целые числа в одну строчку через пробел. Необходимо
преобразовать эти данные в список целых чисел. Затем, перебрать этот список в цикле for и
просуммировать все нечетные значения. Результат вывести на экран.
Пример ввода:
8 11 -2 4 0 13 19 12 7
Пример вывода:
50
''' '''
num2 = list(map(int, input('Введите строку из целых чисел через пробел: ').split()))
sum1 = 0
for i in num2:
    if i % 2 != 0:
        sum1 += i
print(sum1)
''' '''
Задание 6.25. Вводятся названия городов в одну строчку через пробел. Необходимо
преобразовать входные данные в список. Затем, перебрать его циклом for и заменить
значения элементов на длину названия соответствующего города. Результат вывести на
экран в виде последовательности чисел через пробел в одну строчку.
Пример ввода:
Москва Уфа Караганда Тверь Минск Казань
Пример вывода:
6 3 9 5 5 6
''' '''
city = list(input('Введите названия городов через пробел: ').split())
city1 = []
for i in city:
    x = len(i)
    city1.append(x)
print(*city1)
''' '''
Задание 6.26. Вводится натуральное число n. С помощью цикла for найти все делители
этого числа. Найденные делители выводить сразу в строку без формирования списка.
Пример ввода:
12
Пример вывода:
1 2 3 4 6 12
'''