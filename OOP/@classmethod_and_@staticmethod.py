class PlayerCharacter:

 # membership = True                #class object attribute(static)
  def __init__(self,name,age):
    self.name = name               #attribute(dynamic)
    self.age = age


  @classmethod       #decorator 

  def adding (cls,num1,num2):
    return num1 + num2


# player1 = PlayerCharacter('prerak') # we dont have to instantiate class for @classmethod

print(PlayerCharacter.adding(4,5))


############################################################################################################
class PlayerCharacter:

 # membership = True                
  def __init__(self,name,age):
    self.name = name              
    self.age = age


  @classmethod        #used when we care or want to modify class attributes i.e name and age

  def adding (cls,num1,num2):
    return cls('prerak',num1 + num2)   #cls to instantiate an object

player3 = PlayerCharacter.adding(4,5)  #whole new player3 created using @classmethod
print(player3.age)  

############################################################################################################

# @staticmethod
    #def adding (num1,num2):
    #return num1 + num2 

#used when we dont care about class attributes which are (name and age)  :   
 #self.name = name
 #self.age = age 


# https://www.makeuseof.com/tag/python-instance-static-class-methods/      use this link to understand more