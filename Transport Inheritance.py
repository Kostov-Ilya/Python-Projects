str_0 = ''
class Transport:
    def __init__(self, brand):
        self.brand = brand
        self.size = 0
    def drive(self):
        print(self.brand, 'drive')

class Car(Transport):
    def __init__(self, brand):
        super().__init__(brand)
        self.speed = 0
    def Refuel(self):
        print(self.brand, 'Refuel Car')
    def brakes(self):
        print(self.brand, 'brakes Car')

class Bike(Transport):
    def __init__(self, brand):
        super().__init__(brand)
        self.practicality = 0
    def breaks(self):
        print(self.brand, 'breaks Bike')
    def signal(self):
        print(self.brand, 'The bike beeps')

print('---------------------')
print(str_0)
print('Transport Class')
print(str_0)
print('---------------------')
obj1 = Transport('Transport')
obj1.drive()
print('---------------------')
obj2 = Car('Car')
print('Car')
print('---------------------')
obj2.Refuel()
print('---------------------')
obj2.brakes()
print('---------------------')
obj2.drive()
print('---------------------')
obj3 = Bike('Bike')
print('Bike')
print('---------------------')
obj3.breaks()
print('---------------------')
obj3.signal()
print('---------------------')
obj3.drive()