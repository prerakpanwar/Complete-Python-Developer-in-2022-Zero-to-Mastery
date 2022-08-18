#without using Generator
def make_list(num):
  result= []
  for i in range(num):
    result.append(i*2)
  return result

my_list = make_list(10)
print(list(range(50)))
print(my_list)

####################################################
#now with help of Generator

def generator_func(num):
  for i in range(num):
    yield i

for item in generator_func(50):
  print(item)

####################################################
#using next
def generator_func(num):
  for i in range(num):
    yield i*2

g = generator_func(10)        #0*2
next(g)                       #1*2
next(g)                       #2*2
print (next(g))