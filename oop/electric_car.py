from car import CarClass


class Battery:
    def __init__(self, charge=100):
        self.charge = charge
        self.name = 'Батарейка'

    def show_charge_level(self):
        return (f'Уровень {self.charge}')

class ElectricCar(CarClass):
    info = 'Класс с описанием электромобиля'
    def child_method(self):
        print('Метод класса наследника')

    def __init__(self, vendor, model, year=1990):
        super().__init__(vendor, model, year=1990)
        self.battery = '100%'

    def show_fulname(self):
        print(f'{self.vendor} {self.model} {self.year} года выпуска. Заряд {self.battery}')
        #pass

car1 = ElectricCar('Tesla', 's', 2023)
print(car1.vendor)
car1.show_fulname()
car1.child_method()
print(car1.info)
print(car1.battery)