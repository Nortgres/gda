def multiply(x, y):
    product = x * y
    return product


num = multiply(3, 5) # позиционные аргументы
#print(num)


def currency(course, amount): # именованные аргументы
    money = round(amount / course)
    return money


#print(currency(75.5, 10_000))


def currency2(course, amount=1000): # параметры по умолчанию
    money = round(amount / course)
    return money


#print(currency2(75.5, 5_000))
#print(currency2(75.5))

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
#print(double_list2(a))

#def avg(a, b, c):
#    return (a + b +c) / 3
#print(avg(1, 2, 3))

def f3(*args):
    print(args)
    print(type(args), len(args))
    for x in args:
        print(x)

#f3(1, 2, 3)
def avg(*args):
    """Returns the average of a list of numeric values."""
    return sum(args) / len (args)
    #total = 0
    #for i in args:
    #    total += i
    #return total / len(args)

#print(f4(1, 2, 3, 4, 5))

def f5(x, y, z):
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'z = {z}')

t = ('foo', 'bar', 'baz')
#f5(*t)

def f6(*args):
    print(type(args), args)

a = ('foo', 'bar', 'baz')

#f6(*a)

def f7(a, b, *args, **kwargs):
    print(F'a = {a}')
    print(F'b = {b}')
    print(F'args = {args}')
    print(F'kwargs = {kwargs}')

#f7(1, 2, 'foo', 'bar', 'baz', x=1)

def concat(prefix, *args):      #(*args, prefix='-> ')
    print(f'{prefix}{".".join(args)}')

#concat('-> ', 'a', 'b', 'c')    #('a', 'b', 'c', prefix='... ')

# * останавливает ввод позиционных аргументов: def oper(x, y, *, op='+'):

def concat2(*args, prefix='-> ', sep='.'):
    print(f'{prefix}{sep.join(args)}')

#concat2('a', 'b', 'c', prefix='//', sep='-')

# / разрешает позиционные и именные параметры def f(x, y, /, z):   f(1, 2, 3) или f(1, 2, z=3)

def f8(x, y, /, z, w, *, a, b):
    print(x, y, z, w, a, b)

#f8(1, 2, 3, w=4, a=5, b=6)

#help(avg)

def foo(bar=0, baz=1):
    """Perform a foo transformation.

    Keyword arguments:
    :param bar:
    :param baz:
    :return:
    """
#help(foo)

def avg2(*args: float) -> float:
    return sum(args) / len(args)

#help(avg2)

def kinetic_energy(mass: 'in kilograms', velocity: 'in meters per second'):
    pass

# lambda функции
def sqr(x):
    return x*x

s = lambda x: x * x
print(s(5))

plus = lambda x, y: x + y
print(plus(5, 7))

print((lambda x, y, z=3: x + y + z)(1, y=2))

capitals = {'France': 'Paris', 'Canada': 'Ottawa'}
sorted(capitals.items(), key=lambda capital: capital[1])

nums = [50700, 1307, 2040, 200]
print(min(nums, key=lambda s: str(s).count('0')))
print(sorted(nums, key=lambda s: str(s).count('0')))
print(sorted(sorted(nums, key=lambda s: str(s).count('0'))))