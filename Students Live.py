from random import randint
class Student:
	print('Student Life Simulation:')
	def __init__(self, name):
		self.name = name
		self.gladness = 50
		self.progress = 10
		self.money = 30
		self.alive = True
	def education(self, University):
		print(self.name, 'is studying in', University.title)
	def working(self):
		self.gladness -= 10
		self.progress += 5
		self.money += 10
		print('Work Time')
	def Purchases(self):
		self.progress -= 5
		self.gladness += 10
		self.money -= 5
		print('Purchases Time')
	def study(self):
		self.progress += 25
		self.gladness -= 15
		self.money -= 3
		print('Study Time')
	def chill(self):
		self.gladness += 20
		self.progress -= 8
		self.money -= 1
		print('Chill time')
	def sleep(self):
		self.gladness += 4
		self.progress += 1
		print('Sleep time')
	def say_hello(self):
		print('Hello Teacher! Hello Friend! Hello Parents!')
	def live(self):
		live_cube = randint(1,6)
		if live_cube == 1:
			self.study()
		elif live_cube == 2:
			self.chill()
		elif live_cube == 3:
			self.sleep()
		elif live_cube == 4:
			self.say_hello()
		elif live_cube == 5:
			self.working()
		elif live_cube == 6:
			self.Purchases()
		self.final()
	def final(self):

		if self.progress == 100:
			print('/Amazing! You graduated!')
			self.alive = False

		elif self.progress < -20:
			print('/Too bad... You didn`t graduate!')
			self.alive = False

		elif self.gladness < -20:
			print('/Depression...')
			self.alive = False

		elif self.money < -20:
			print('/You became a poor student...')
			self.alive = False

class University:
	def __init__(self, title):
		self.specialization = 'None'
		self.address = 'None'
		self.title = title
		self.descriptopn = 'None'
	def study(self, Student):
		print(Student.name, 'is studying')
	def pay_for_study(self, Mother):
		print(Mother.name,'paid for study')

class Mother:
	def __init__(self, name):
		self.name = name
	def argue(self):
		print("I'm angry!!!")

print('Bob\'s life')
obj1 = Student('Bob')
for i in range(365):
	if obj1.alive == False:
		break
	obj1.live()

print('Jane\'s life')
obj2 = Student('Jane')
for i in range(365):
	if obj2.alive == False:
		break
	obj2.live()

univer = University('Oxford')
univer.study(obj2)
obj2.education(univer)

mom = Mother('Chloe')
mom.argue()
univer.pay_for_study(mom)

