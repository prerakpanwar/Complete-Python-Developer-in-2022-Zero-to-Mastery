class User:
    def login(self):
        print('login successful')


class Wizard(User):  										#sub class of User class #inheritance
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):  										#sub class of User class #inheritance
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran very fast')


class Oger(Wizard, Archer):   								#multiple inheritance                        
    def __init__(self, name, power, arrows):				#multiple inheritance made code complex on line 28,29,30
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


oger1 = Oger('shrek', 50, 100)
print(oger1.login())
print(oger1.attack())
print(oger1.check_arrows())
print(oger1.run())


		  