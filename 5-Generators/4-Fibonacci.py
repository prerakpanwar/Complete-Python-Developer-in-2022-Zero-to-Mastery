#using Generator

def fib(num):
  a = 0
  b = 1
  for i in range(num):
    yield a
    temp = a
    a = b
    b = temp + b

for item in fib(20):
  print (item)


#using List

def fib2(num):
  a = 0
  b = 1
  result = []
  for i in range(num):
    result.append(a)
    temp = a
    a = b
    b = temp + b
  return result

print (fib2(20))