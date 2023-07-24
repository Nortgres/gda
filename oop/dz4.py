'''Объявите класс с именем TravelBlog и объявите в нем атрибут:
total_blogs: 0
У объектов должны быть атрибуты name и days
Пример
name: 'Франция'
days: 6
Увеличьте значение атрибута total_blogs класса TravelBlog на единицу при создании объекта.
добавьте метод который бы показывал текущее значени total_blogs
Создайте несколько объектов и вывидите на экран значени total_blogs'''
class TravelBlog:

    total_blogs = 0

    def __init__(self, name, days):
        self.name = name
        self.days = days
        TravelBlog.total_blogs += 1

    def print_total_blogs(self):
        print(f'{TravelBlog.total_blogs}')


TravelBlog1 = TravelBlog('Франция', 6)
TravelBlog2 = TravelBlog('Франция', 6)
TravelBlog3 = TravelBlog('Франция', 6)
TravelBlog4 = TravelBlog('Франция', 6)
TravelBlog5 = TravelBlog('Франция', 6)
TravelBlog1.print_total_blogs()
TravelBlog2.print_total_blogs()
TravelBlog3.print_total_blogs()
TravelBlog4.print_total_blogs()
TravelBlog5.print_total_blogs()

'''Объявите класс с именем Person и атрибутами:
name: 'Юрий Тверской'
job: 'Писатель'
city: 'Иваново'
Создайте экземпляр этого класса и проверьте, существует ли у него локальное свойство с
именем job. Выведите True, если оно присутствует в объекте и False - если отсутствует(или равно пустой строке)'''

class Person:


    def __init__(self, name, job, city):
        self.name = name
        self.job = job
        self.city = city

    def print_check_job(self):
       if self.job != None: print(f'True')
       else: print('False')

Person1 = Person('Юрий Тверской', 'Писатель', 'Иваново')
Person2 = Person('Юрий Тверской', None, 'Иваново')
Person1.print_check_job()
Person2.print_check_job()