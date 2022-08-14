def sum(a,b):
  try:
    return a / b

#to give meaningful errors to users
  except TypeError as var:   
    print(var)

print(sum('a',3))

######################################################################################
def sum(c,d):
  try:
    return c / d

#for handling different errors the same way
  except (TypeError , ZeroDivisionError):
    print('oops')
#OR except (TypeError , ZeroDivisionError) as var: print(var)


print(sum('a',3))       # for checking TypeError
print(sum(3,0))         # for checking ZeroDivisionError