class Soda:

    def __init__(self, dop=None):
        self.dop = dop

    def show_my_drink(self):
        if self.dop != None:
            print(f'Газировка и {self.dop}')
        else:
            print(f'Обычная газировка')


drink1 = Soda('Лимон')
drink2 = Soda()
drink1.show_my_drink()
drink2.show_my_drink()