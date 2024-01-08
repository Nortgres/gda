class Dog:
                                   # док.строка
    species = "Ganis familiaris"   # атрибуты класса
    def __init__(self, name, age): # атрибуты экземпляра
        self.name = name
        self.age = age

    # методы класса - функция встроенная в класс
    # с помощью метода __str__ переопределяет вывод print класса
