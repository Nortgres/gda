class Thing:
    id_counter = 0

    def __init__(self, name, price):
        self.id = Thing.id_counter
        Thing.id_counter += 1
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None


class PhysicalThing(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElectronicThing(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm
thing1 = PhysicalThing('Книга', 1000.0, 0.5, (20.0, 15.0, 3.0))
print(thing1.id)  # 0
print(thing1.name)  # Книга
print(thing1.price)  # 1000.0
print(thing1.weight)  # 0.5
print(thing1.dims)  # (20.0, 15.0, 3.0)
print(thing1.memory)  # None
print(thing1.frm)  # None

thing2 = ElectronicThing('Электронная книга', 500.0, 1000000, 'pdf')
print(thing2.id)  # 1
print(thing2.name)  # Электронная книга
print(thing2.price)  # 500.0
print(thing2.weight)  # None
print(thing2.dims)  # None
print(thing2.memory)  # 1000000
print(thing2.frm)  # pdf

thing3 = PhysicalThing('Книга', 1000.0, 0.5, (20.0, 15.0, 3.0))
print(thing3.id)
thing4 = PhysicalThing('Книга', 1000.0, 0.5, (20.0, 15.0, 3.0))
print(thing4.id)