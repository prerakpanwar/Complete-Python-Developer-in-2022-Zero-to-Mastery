class PlayerCharacter:
  def __init__(self,name):
    self.name = name

  def run (self):
    print('run')

player1 = PlayerCharacter('prerak')
player2 = PlayerCharacter('panwar')

print(player1.name)
print(player2.name)