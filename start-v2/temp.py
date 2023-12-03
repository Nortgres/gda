def decorator1(func):
    def wrapper1(*args, **kwargs):
        print("Декоратор 1 до вызова функции")
        result = func(*args, **kwargs)
        print("Декоратор 1 после вызова функции")
        return result
    return wrapper1

def decorator2(func):
    def wrapper2(*args, **kwargs):
        print("Декоратор 2 до вызова функции")
        result = func(*args, **kwargs)
        print("Декоратор 2 после вызова функции")
        return result
    return wrapper2

def decorator3(func):
    def wrapper3(*args, **kwargs):
        print("Декоратор 3 до вызова функции")
        result = func(*args, **kwargs)
        print("Декоратор 3 после вызова функции")
        return result
    return wrapper3

@decorator1
@decorator2
@decorator3
def my_function():
    print("Выполнение функции")

my_function()