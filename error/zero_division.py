try:
    print(5/1)
    print(5/5)
except ZeroDivisionError:
    print('на ноль делить нельзя')
except TypeError:
    print('Можно передавать только числа')
except:
    print('Непредвиденная ошибка')
else:
    print('Ошибок нет')
finally:
    print('Выполняется в любом случае')