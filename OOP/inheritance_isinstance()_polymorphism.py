class User:
	def login(self):
		print('login successful')

class Wizard(User):                                #sub class of User class #inheritance
		def __init__ (self,name,power):
			self.name = name
			self.power = power
		def attack(self):
			print(f'attacking with power of {self.power}')

class Archer(User):								   #sub class of User class #inheritance
		def __init__ (self,name,num_arrows):
			self.name = name
			self.num_arrows = num_arrows
		def attack(self):
			print(f'attacking with arrows and arrows left are: {self.num_arrows}')

Wizard1 = Wizard('Prerak',100)
Archer1 = Archer('panwar',50)
Archer1.attack()                           # polymorphism : same function name but used for different work/output
Wizard1.attack()						   # polymorphism : same function name but used for different work/output
Wizard1.login()
Archer1.login()


print(isinstance(Wizard1,Wizard))         #checking if Wizard1 is an instance of class Wizard
print(isinstance(Wizard1,User))			  #Wizard1 is an instance of class User too as User is parent class of Wizard
print(isinstance(Wizard1,object))		  #Wizard1 is also an instance of class Object as Object is parent class of User class i.e class user (object)