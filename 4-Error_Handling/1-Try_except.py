while True:

  try:
    age = int(input('what is your age? '))
    result = 10/age
  except ValueError:
    print('please enter a number')
  except ZeroDivisionError:
    print('please enter a number greater than 0')
  else:
    print('thanks')
    break