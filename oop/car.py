class CarClass:
    info = 'Описание класса Машина'


    def __init__(self, vendor, model, year=1990):
        self.vendor = vendor
        self.model = model
        self.year = year
        self.odometr = 0

    def show_fulname(self):
        print(f'{self.vendor} {self.model} {self.year} года')

    def update_odometr(self, km):
        if km <= 0:
            print('Недопустимое значение')
        else:
            self.odometr += km
            print(f'Новый пробег {self.odometr} км')

    def move(self, km):
        if km <= 0:
            print('Недопустимое значение')
        else:
            print(f'Проехали {km}')
            self.update_odometr(km)
            print(f'Новый пробег {self.odometr} км')

CarClass.info = "New Описание класса Машина"
car1 = CarClass('LADA','2109')
car2 = CarClass('ГАЗ',model=3110)

#car1.vendor = 'LADA'
#car2.vendor = 'ГАЗ'

'''print(car1.vendor, car1.model, car1.year)
car2.show_fulname()
car1.update_odometr(-100)
car1.update_odometr(200)
#car1.odometr += 11 #не рекомендуестся
print(car1.odometr)
car1.move(500)'''