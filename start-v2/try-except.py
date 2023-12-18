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
text = input('Введите текст: ').split()

def nums(text):
    try:
        int(text) / 1
        return True
    except ValueError:
        return False

x = sum(map(int, (filter(nums, text))))
print(x)
