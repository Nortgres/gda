'''Задание 3.16. Вводятся:
• названия городов в одну строчку через пробел, на основе этой строки формируется список;
• название нового города.
Необходимо вставить во вторую позицию этого списка новый город и вывести список на экран с распаковкой.
Пример ввода:
Москва Казань Ярославль
Ульяновск
Пример вывода:
Москва Ульяновск Казань Ярославль'''
########################################################
'''list1 = (input('Введите список городов (через пробел): ')).split()
list1.insert(1, (input('Введите название нового города: ')))
text1 = ' '.join(list1)

print(text1)'''
########################################################
'''Задание 3.17. Вводится информация по книге (каждое значение с новой строки): название,
автор, число страниц (целое число), цена (вещественное число). На основе этих данных
формируется список с элементами в порядке их ввода. Затем, из этого списка необходимо
удалить число страниц, в качестве автора записать "Пушкин" и цену увеличить в 2 раза.
Результат вывести на экран.
Пример ввода:
Мастер и Маргарита
Булгаков
233
435.45
Пример вывода:
['Мастер и Маргарита', 'Пушкин', 870.9]'''
########################################################
'''n_book = input('Введите название книги: ')
a_book = input('Введите автора книги: ')
k_book = int(input('число страниц (целое число): '))
p_book = float(input('цена (вещественное число): '))
l_book = [n_book, a_book, k_book, p_book]
l_book.remove(k_book)
l_book[1] = 'Пушкин'
l_book[2] = p_book*2

print(l_book)'''
#######################################################
'''Задание 3.18. Вводится число новых подписчиков канала по дням в одну строку через
пробел. На основе введенной строки необходимо сформировать список из целых чисел.
Требуется отсортировать элементы этого списка по убыванию и результат вывести на экран.
Пример ввода:
52 65 64 54 68 59 42 63
Пример вывода:
68 65 64 63 59 54 52 42'''
########################################################
'''list3 = (input('Вводится число новых подписчиков канала (через пробел): ')).split()
list3 = list(map(int, list3))
list3.sort(reverse=True)
print(list3)'''
########################################################
'''Задания к разделу 1.3
Задание 3.19. Вводится строка с номером телефона в формате:
+7(xxx)xxx-xx-xx
Необходимо преобразовать ее в список (посимвольно, то есть, элементами списка будут
являться отдельные символы строки). Затем, удалить первый '+', число 7 заменить на 8 и
убрать дефисы. Далее преобразовать этот список в строку и вывести на экран.
Пример ввода:
+7(910)234-50-56
Пример вывода:
8(910)2345056'''
########################################################
'''list4 = list(input('Введите номер телефона: '))
del list4[0:2]
list4.insert(0,8)
list4 = list(filter(lambda i: i != '-', list4))
print(''.join(map(str, list4)))'''
########################################################
'''Задание 3.20. Вводятся целые числа в одну строчку через пробел (не менее четырех).
Необходимо найти три наименьших числа в этой последовательности чисел и вывести их на
экран в порядке возрастания. Реализовать программу без использования срезов или
условного оператора.
Пример ввода:
8 11 -5 10 -1 0 7
Пример вывода:
-5 -1 0
'''
########################################################
'''list5 = (input('Введите целые числа в одну строчку через пробел: ')).split()
list5 = list(map(int, list5))
list5.sort()
print(f'{list5[0]} {list5[1]} {list5[2]}')'''
########################################################
'''Задание 3.21. Вводятся целые числа в одну строчку через пробел. Необходимо
преобразовать их в список , затем, удалить последнее значение и если оно нечетное, то в
список (в конец) добавить True, иначе - False. Отобразить полученный список на экране с
распаковкой. Реализовать программу без использования условного оператора.
Пример ввода:
8 11 0 3 5 6
Пример вывода:
8 11 0 3 5 False
'''
########################################################
list6 = (input('Введите целые числа в одну строчку через пробел: ')).split()
list6 = list(map(int, list6))
r = list6.pop()
list6.append(lambda r: r%2 == 0)
print(list6)

########################################################
'''Задание 3.22. Вводятся оценки студента (целые числа) в одну строку через пробел (не
менее 8 оценок). Необходимо определить количество двоек и вывести это значение на
экран.
Пример ввода:
2 3 5 2 4 2 2 5
Пример вывода:
4

list10 = (input('Введите оценки студента (целые числа) в одну строку через пробел: ')).split()
list10 = list(map(int, list10))
print (list10)
'''
