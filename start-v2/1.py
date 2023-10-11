#cities = ['Dubai', 'Milan', 'Miami', 'Paris', 'Tokyo']
#del cities[1], cities[3]
#print(cities)

#cities = ('Dubai', 'Milan', 'Miami', 'Paris', 'Tokyo')
#print(cities)


'''tuple1 = (5.45, -18.9)
tuple1 = tuple1 + tuple(map(int, input('Введите числа через пробел: ').split()))
print(tuple1)

tuple2 = tuple(input('Введите названия городов: ').split())
city = 'Москва'
tuple3 = (city, ) * (city not in tuple2)
tuple4 = tuple2 + tuple3
print(tuple4)

tuple5 = tuple(input('Введите названия городов: ').split())
tuple6 = tuple5[:-2]+tuple5[-1:]
print(tuple6)

tuple7 = tuple(input('Введите имена студентов: ').split())
print(tuple7.count(input('Введите имя: ')))

tuple8 = tuple(map(int, input('Введите оценки студентов: ').split()))
num = sum(tuple8) / len(tuple8)
print(round(num, 1))

tuple9 = tuple(input('Введите названия городов: ').split())
city = input('Введите название города: ')
a = tuple9.index(city)
print(tuple9[a::2])

#задание 4.7
tuple10 = tuple(map(int, input('Введите оценки студентов: ').split()))
print(tuple10[6:1:-1)

#задание 4.8
tuple11 = tuple(map(int, input('Введите первый набор чисел: ').split()))
tuple12 = tuple(map(int, input('Введите первый набор чисел: ').split()))
tuple13 = tuple(map(int, input('Введите первый набор чисел: ').split()))
tuple14 = (tuple11, tuple12, tuple13)
print(tuple14[0][-1]+tuple14[1][-1]+tuple14[2][-1])

#задание 4.9
tuple15 = tuple(map(float, input('Введите длину, ширину и высоту параллелепипеда: ').split()))
volume = tuple15[0]*tuple15[1]*tuple15[2]
n = round(volume, 2)
print(f'{n:_}')
'''
#задание 4.10
tuple16 = tuple(map(int, input('Введите первый набор чисел: ').split()))
tuple17 = tuple(map(int, input('Введите первый набор чисел: ').split()))
tuple18 = tuple(map(int, input('Введите первый набор чисел: ').split()))
tuple19 = (tuple16, tuple17, tuple18)
x1 = sum(tuple19[0])/len(tuple19[0])
x2 = sum(tuple19[1])/len(tuple19[1])
x3 = sum(tuple19[2])/len(tuple19[2])
print(f'{round(x1, 1)} {round(x2, 1)} {round(x3, 1)}')
