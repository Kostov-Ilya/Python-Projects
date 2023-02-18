str_0 = ''
class Literature:
    def __init__(self, name):
        self.name = name
        self.size = 0

    def Read(self):
        print(self.name, 'Read')

class Book(Literature):
    def __init__(self, name):
        super().__init__(name)
        self.Length = 0
    def Learning(self):
        print(self.name, 'Learning Book')
    def Obsolescence(self):
        print(self.name, 'Obsolescence Book')

class Magazine(Literature):
    def __init__(self, name):
        super().__init__(name)
        self.Width = 0
    def Reliability(self):
        print(self.name, 'Reliability of Information')
    def Examination(self):
        print(self.name, 'Examination Examination')


print('---------------------')
print(str_0)
print('Literature Class')
print(str_0)
print('---------------------')
obj1 = Literature('Human')
obj1.Read()
print('---------------------')
obj2 = Book('Book')
obj2.Learning()
print('---------------------')
obj2.Obsolescence()
obj3 = Magazine('Magazine')
print('---------------------')
obj3.Reliability()
print('---------------------')
obj3.Examination()
print('---------------------')