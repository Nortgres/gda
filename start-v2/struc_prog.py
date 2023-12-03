'''
w = 5
def func():
    w = 7
    print(w)

func()
print(w)
'''
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

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
#say_whee()

#####
'''
def not_higth(func):
    def wrapper():
        #if 7 <= datetime.now().hour < 22:
        func()
        #else:
        #    pass #Тише, соседи спят
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_higth(say_whee)
'''
####

'''
#say_whee2()

@my_decorator
def say_whee():
    print("Whee!")


def my_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper()

say_whee()

'''
'''
def my_dec(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

#print(return_greeting("Adam"))
'''
