'''for x in range(1, 4):
    for y in range(3, 6):
        print(f'{x} {y}')

array = [[5, 10, 15, 20], [3, 6, 9, 12], [7, 14, 21, 28]]
for x in range(len(array)):
    for y in range(len(array[x])):
        print(f'{array[x][y]:2}', end=' ')
    print()

cities = ['Dubai', 'Milan', 'Miami', 'Paris', 'Tokyo']
for i, city in enumerate(cities, 1):
    print(f'{i} - {city}')

a = [5, 6, 7, 10, 12]
for i, x in enumerate(a):
    if x % 2 == 0:
        a[i] += 1
print(a)

cities = ['Dubai', 'Milan', 'Miami', 'Paris', 'Tokyo']
iter_cities = iter(cities)
for i in range(len(cities)+1):
    print(next(iter_cities, 'The end'))

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits if 'a' in x]
print(newlist)

list1 = [x**2 for x in range(10)]
print(list1)

original_prices = [1.25, 0.85, 10.22, 3.78, 0.92, 1.16]
prices = [i if i > 1 else 1.0 for i in original_prices]
print(prices)

newlist2 = [x.upper() for x in fruits]
print(newlist2)

text = 'Барабанщик бил бой в барабан'
x = -1
for i in range(text.count('ра')):
    k = text.index('ра', x+1)
    print(k, end=' ')
    x = k
'''
text = 'Барабанщик бил бой в барабан'
list1 = list(text)
for i in list1:
    if i == 'р':
        print(list1{i})