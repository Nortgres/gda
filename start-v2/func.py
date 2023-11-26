def multiply(x, y):
    product = x * y
    return product


num = multiply(3, 5) # позиционные аргументы
print(num)


def currency(course, amount): # именованные аргументы
    money = round(amount / course)
    return money


print(currency(75.5, 10_000))


def currency2(course, amount=1000): # параметры по умолчанию
    money = round(amount / course)
    return money


print(currency2(75.5, 5_000))
print(currency2(75.5))

def double_list(x):
    i = 0
    while i < len(x):
        x[i] = i**2
        i += 1

def double_list2(x):
    r = []
    for i in x:
        r.append(i**2)
    return r


a = [1, 2, 3]
print(double_list2(a))

