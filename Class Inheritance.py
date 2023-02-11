str_1 = ' '
class Human:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.strenght = 0
    def live(self):
        print(self.name, 'Living')
    def eat(self):
        print(self.name, 'Eating')

class Teacher(Human):

    def __init__(self, name):
        super().__init__(name)
        self.iq = 0
    def Learn(self):
        print(self.name, 'Learn Children')
    def Work(self):
        print(self.name, 'Working')

class Student(Human):
    def __init__(self, name):
        super().__init__(name)
        self.activity = 0
    def Learning(self):
        print(self.name, 'Learning Lessons')
    def Homework(self):
        print(self.name, 'Do Homework')

print('Human Class')
print(str_1)
obj1 = Human('Human')
obj1.live()
print('-----------------------')
obj1.eat()
print('***********************')
print('Teacher Class')
print(str_1)
obj2 = Teacher('Andrey')
print('-----------------------')
obj2.live()
print('-----------------------')
obj2.eat()
print('-----------------------')
obj2.Learn()
print('-----------------------')
obj2.Work()
print('***********************')
print('Student Class')
print(str_1)
obj3 = Student('Vlad')
print('-----------------------')
obj3.live()
print('-----------------------')
obj3.eat()
print('-----------------------')
obj3.Learning()
print('-----------------------')
obj3.Homework()

