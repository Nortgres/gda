'''
w = 5
def func():
    w = 7
    print(w)

func()
print(w)
'''
import sys

'''
w = 5
v = 'A'
#def func():
  #  print(w, v)

#func()

#sqr.__code__.co_varnames
#('base', 'result')

#sqr.__code__.co_name
#'sqr'

#sqr.__code__.co_argcount

def avgpow(lst, power=2):
    def avg():
        result = sum(lst) / len(lst)
        return result
    result = avg() ** power
    return result
#print(avgpow([2, 3, 4]))
#print(avgpow([2, 3, 4], 3))

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Hey {name}, together we are awesome!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

#print(say_hello('John'))
#print(be_awesome('John'))
#print(greet_bob(say_hello))
#print(greet_bob(be_awesome))
'''
'''
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")
    second_child()
    first_child()
parent()
'''
'''
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Hi, I am Liam"
    if num == 1:
        return first_child
    else:
        return second_child

#print(parent(1))
#print(parent(2))

first = parent(1)
second = parent(2)
#print(first)
#print(second)
#print(first())
#print(second())

# замыкание
def multiply(num1):
    var = 10
    def inner(num2):
        return num1 * num2
    return inner
mult_by_5 = multiply(5)

#print(mult_by_5.__closure__[0].cell_contents)
#print(mult_by_5(10))

mult_by_7 = multiply(7)
#print(mult_by_7(10))
'''
# декораторы функций
'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()

#####

from datetime import datetime
def not_higth(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass #Тише, соседи спят
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_higth(say_whee)
say_whee()
'''

####
# @my_decorator - Это более простая запись say_whee = my_decorator(say_whee)
'''
def my_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(name):
    print(f"Hello {name}")


greet('World')
'''

'''
def my_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("Adam")
print(hi_adam)
'''
'''
def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs) 
        # Do something 
        xxxxx
'''
'''
import time
def timer(func):
    """Print the runtime of the decorated function"""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() #1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()   #2
        run_time = end_time - start_time #3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(999)
'''
'''
import timeit
print(timeit.timeit('for x in range(100): lambda x: x * x', number=100000))

def f(x):
    return x * x
t = timeit.repeat("for x in range(100): f(x)", "from __main__ import f", number=100000, repeat=3)
print(sum(t) / len(t))
print(t)
'''
'''
# декоратор для отладки
def debug(func):
    """Print the function signature and return value"""
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                     #1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()] #2
        signature = ", ".join(args_repr + kwargs_repr)          #3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")          #4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


#print(make_greeting("Benjamin"), "\n")
#print(make_greeting("Benjamin", age=112))

import math
math.factorial = debug(math.factorial)
def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))
#print(approximate_e(6))
'''
'''

import functools
def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

def debug(func):
    """Print the function signature and return value"""
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

@debug
@do_twice
def greet(name):
    print(f"Hello {name}")


greet("Eva")


@do_twice
@debug
def greet(name):
    print(f"Hello {name}")


greet("Iva")
'''
'''
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
greet("World")

def generate_power(exponent):
    def power(func):
        def inner_power(*args):
            base = func(*args)
            return base ** exponent
        return inner_power
    return power


@generate_power(2)
def raise_tho(n):
    return n

@generate_power(3)
def raise_three(n):
    return n

print(raise_tho(5))
print(raise_three(5))
'''

'''
# Генераторы
# print(f'{sys.getsizeof([x for x in range(1_000)]):_} bytes')
# print(f'{sys.getsizeof([x for x in range(1_000_000)]):_} bytes')
# print(f'{sys.getsizeof([x for x in range(100_000_000)]):_} bytes')
ge = (s for s in 'Python')
#print(ge)
#print(next(ge))
#print(next(ge))

nums_squared_lc = [num**2 for num in range(5)]
nums_squared_ge = (num**2 for num in range(5))
#print(nums_squared_lc)
#print(nums_squared_ge)
#print(list(nums_squared_ge))

#print(sum(nums_squared_lc))
#print(sum(nums_squared_ge))

nums_squared_ge = (num**2 for num in range(5))
#print(sum(nums_squared_ge))

def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen = mygenerator()
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(f'{sys.getsizeof(gen):_} bytes')


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

def fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a+b
f = fib()
print(next(f))
print(next(f))
print(next(f))

#while 1:
#    print(next(f))
'''
# Основы функционального программирования
'''
numbers = [1, 2, 3, 4, 5]
squared = []
#for num in numbers:
#    squared.append(num ** 2)
#print(squared)

def squre(number):
    return number ** 2
#for num in numbers:
#    squared.append(squre(num))

#squared = map(squre, numbers)
squared = map(lambda num: num ** 2, numbers)
print(list(squared))

base = [5, 5, 7, 10, 10]
exponent = [3, 4, 2, 2, 3]
rez = list(map(lambda num, exp: num ** exp, base, exponent))
print(rez)
print(list(map(lambda x, y, z: x + y + z, [2, 4, 5], [1, 3], [7, 8, 9])))

string_it = ["processing", "strings", "with", "map"]
print(list(map(str.capitalize, string_it)))
print(list(map(str.upper, string_it)))
print(list(map(str.lower, string_it)))

numders = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: (x, x**2, x**3), numders)))

def to_farenheit(c):
    return 9 / 5 * c + 32
def to_celsius(f):
    return (f - 32) * 5 / 9
celsius_temp = [100, 40, 80]
print(list(map(to_farenheit, celsius_temp)))

fahr_temps = [212, 104, 176]
print(list(map(to_celsius, fahr_temps)))

numbers2 = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x ** 2, numbers2)))
print([x ** 2 for x in numbers2])

numbers3 = [-2, -1, 0, 1, 2]
def extract_positive(numbers):
    positive_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers

print(list(filter(lambda n: n > 0, numbers3)))
def is_positive(n):
    return n > 0
print(list(filter(is_positive, numbers3)))

numbers4 = [1, 3, 10, 45, 6, 50]
def extract_even(numbers):
    event_numbers = []
    for number in numbers:
        if number % 2 == 0:
            event_numbers.append(number)
    return event_numbers
print(extract_even(numbers4))

print(list(filter(lambda number: number % 2 == 0, numbers4)))
print([number for number in numbers4 if not number % 2])

words = ("filter", "Ana", "hello", "world", "madam", "racecar")
print(list(filter(lambda w : w.lower() == "".join(reversed(w)).lower(), words)))
print([w for w in words if w.lower() == "".join(reversed(w)).lower()])
print(list(w for w in words if w.lower() == "".join(reversed(w)).lower()))

def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result
print(my_add(5,5))

from functools import reduce
numbers5 = [0, 1, 2, 3, 4, 5]
print(reduce(my_add, numbers5))
print(reduce(lambda a, b: a + b, numbers5))

from operator import add
print(add(1, 2))
print(reduce(add, numbers5))

print(reduce(lambda a, b: a * b, numbers5))

numbers6 = [1, 2, 3, 4, 5]
from operator import mul
print(mul(2, 2))
print(reduce(mul, numbers6))

from math import prod
print(sum(numbers6))
print(prod(numbers6))
'''

from functools import reduce
from timeit import timeit

def add(a, b):
    return a + b
use_add = "functools.reduce(add, range(100))"
##print(timeit(use_add, "import functools", globals={"add": add}))
use_lambda = "functools.reduce(lambda x, y: x + y, range(100))"
##print(timeit(use_lambda, "import functools"))

use_operator_add = "functools.reduce(operator.add, range(100))"
##print(timeit(use_operator_add, "import functools, operator"))
##print(timeit("sum(range(100))", globals={"sum": sum}))

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(zipped)
print(type(zipped))
print(list(zipped))

fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
a_dict = dict(zip(fields,values))
print(a_dict)