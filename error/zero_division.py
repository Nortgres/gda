try:
    print(5/'a')
    print(5/0)
except ZeroDivisionError:
    print('на ноль делить нельзя')
except TypeError:
    print('Можно передавать только числа')
except:
    print('Непредвиденная ошибка')
