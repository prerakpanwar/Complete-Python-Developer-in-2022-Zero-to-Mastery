class Mygen:
  current = 0
  def __init__ (self, first, last):
    self.first = first
    self.last = last
    # Mygen.current = self.first #this line allows us to use the current number as the starting point for the iteration


  def __iter__(self):
    return self

  def __next__ (self):
    if Mygen.current < self.last:
      num = Mygen.current
      Mygen.current +=1
      return num
    raise StopIteration

g = Mygen(0,100)
for i in g:
  print(i)


####################
def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      print(iterator)
      print(next(iterator)*2)
    except StopIteration:
      break

special_for([1,2,3])
