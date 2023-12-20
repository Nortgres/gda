x = 10
# if x > 5:
#    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# try:
#    10 / 0
# except:
#    pass
# print('error!')

# try:
#    10 / 0
# except Exception as error:
#    print('Возникла ошибка:', error)

# try:
#    with open('file.log') as file:
#        read_data = file.read()
# except Exception as error:
#    print(error)

# try:
#    with open('file.log') as file:
#        read_data = file.read()
# except FileNotFoundError as fnf_error:
#    print(fnf_error)

# try:
#    with open('file.log') as file:
#        read_data = file.read()
#        file.write('Hello')
# except FileNotFoundError as error:
#    print(error)
# except OSError as error:
#    print(error)

# try:
# run this code
# except:
# error
# else:
# if not error
# finally:
# Always run this code.
'''
try:
    with open('file.log', 'r+') as file:
        read_data = file.read()
        file.write('Hello')
except FileNotFoundError as error:
    print(error)
except OSError as error:
    print(error)
else:
    print('Данные успешно сохранены.')
'''
'''
try:
    with open('file.log', 'r+') as file:
        read_data = file.read()
        file.write('Hello')
except FileNotFoundError as error:
    print(error)
except OSError as error:
    print(error)
else:
    print('Данные успешно сохранены.')
finally:  # сработает в любом случае.
    print('Работа программы завершена.')
'''
'''
Задание 13.1. В программе вводятся в одну строчку через пробел некоторые данные,
например: 1 -5.6 2 abc 0 False 22.5 hello world
Эти данные разбиваются по пробелу и представляются в виде списка строк.
Ваша задача посчитать сумму всех целочисленных значений, присутствующих в списке.
Результат (сумму) вывести на экран.
Подсказка: отбор только целочисленных значений можно выполнить с помощь функции
filter() с последующим их преобразованием в целые числа с помощью функции map() и,
затем, вычислением их суммы с помощью функции sum(). Для отбора целочисленных
значений рекомендуется объявить вспомогательную функцию, которая бы возвращала True
для строк, в которых присутствует целое число и False - для всех остальных строк.
Пример ввода:
8 11 abcd -7.5 2.0 -5
Пример вывода:
14
'''
'''
text = input('Введите текст: ').split()

def nums(text):
    try:
        int(text) / 1
        return True
    except ValueError:
        return False

x = sum(map(int, (filter(nums, text))))
print(x)
'''
'''
Задание 13.2. В программе вводятся в одну строчку через пробел некоторые данные,
например: 1 -5.6 True abc 0 23.56 hello
Эти данные разбиваются по пробелу и представляются в виде списка строк.
Ваша задача сформировать новый список, в котором строки с целыми числами будут
представлены как целые числа (тип int), строки с вещественными числами, как
вещественные (тип float), а остальные данные - без изменений.
Реализовать эту задачу следует с помощью функции map() и объявления вспомогательной
функции с механизмом обработки исключений для непосредственного преобразования
данных в целые или вещественные числа.
Пример ввода:
1 -5.6 True abc 0 23.56 hello
Пример вывода:
[1, -5.6, 'True', 'abc', 0, 23.56, 'hello']
'''
'''
text = input("Введите текст: ").split()

def num(text):
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return text


res = list(map(num, text))
print(res)
'''
'''
Задание 13.3. В программе вводятся два значения в одну строку через пробел. Значениями
могут быть числа, слова, булевы величины (True/False). Необходимо прочитать эти
значения из входного потока. Если оба значения являются числами, то вычислить их сумму,
иначе соединить их в одну строку с помощью оператора + (конкатенации строк). Результат
вывести на экран (в блоке finally).
P.S. Реализовать программу с использованием блоков try/except/finally.
Пример ввода 1:
8 11
Пример вывода 1:
19
Пример ввода 2:
5.2 7.1
Пример вывода 2:
12.3
Пример ввода 3:
cat 5
Пример вывода 3:
cat5
'''
try:
    a, b = input('Введите данные: ').split()
    res = 0
    try:
        res = int(a) + int(b)
    except ValueError:
        try:
            res = float(a) + float(b)
        except ValueError:
            res = a + b
finally:
    print(res)
