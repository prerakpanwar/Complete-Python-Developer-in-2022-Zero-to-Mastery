#passing as many arguments/keyword arguments as we want in hello()

#decorator pattern from line (5-10)

def my_decorator(func):
  def wrap_func(*args,**kwargs):
    print('*************')
    func(*args,**kwargs)
    print('*************')
  return wrap_func


@my_decorator
def hello(greetings, emoji):
  print(greetings,emoji)


@my_decorator
def bye(greetings, emoji= ':('):
  print(greetings,emoji)


hello('hello',':)')
bye('byeeee')


