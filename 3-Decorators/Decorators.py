def my_decorator(func):
  def wrap_func():
    print('*************')
    func()
    print('*************')
  return wrap_func

@my_decorator
def hello():
  print('helloooo')
  
@my_decorator
def bye():
  print('byeeeeeeeeeee')

hello()     
#super boosted our hello() using decorator without permanently modifying our hello() 

bye()

#this is how decorator is running 
#but we dont use this as we already have our decorator
a = my_decorator(hello)     #OR my_decorator(hello)()
a()        