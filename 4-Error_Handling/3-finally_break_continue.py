while True:

  try:
    age = int(input('what is your age? '))
    result = 10/age
  except ValueError:
    print('please enter a number')
    continue
  except ZeroDivisionError:
    print('please enter a number greater than 0')
    break
  else:
    print('thanks')
  finally:
    print('ok,i m finally done')
  print('can you hear me?')