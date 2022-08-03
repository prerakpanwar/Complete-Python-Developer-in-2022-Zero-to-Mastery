class PlayerCharacter:

  membership = True                #class object attribute(static)
  def __init__(self,name):
    self.name = name               #attribute(dynamic)

  def run (self):
    print('run')

player1 = PlayerCharacter('prerak')
player2 = PlayerCharacter('panwar')

print(player1.membership)
print(player2.membership)



class Player:

  membership = True                

  def __init__(self,name):
    if (self.membership):            #OR if (Player.membership):
      self.name = name               

  def run (self):
    print('run')

player1 = Player('prerak')
player2 = Player('panwar')

print(player1.name)
print(player2.membership)