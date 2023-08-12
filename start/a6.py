#2023.07.06

'''def key_args(**kwargs):
    print(kwargs)'''

#key_args(arg1=1, arg2=2, arg3=3)

'''def pets_name(owner, **pets):
    print(f'Имя:{owner}')
    for pet, name in pets.items():
        print(f'{pet}:{name}')
pets_name(owner='Петр', кот='Барсик', собака='Бим')

'''

def func1():
    print('Внутренняя ф1')

def func2():
    print('Внутренняя ф2')

####if __name__ == "_main_":  не работает!
def func3():
    print('Основная ф')
    func1()
    func2()
func3()