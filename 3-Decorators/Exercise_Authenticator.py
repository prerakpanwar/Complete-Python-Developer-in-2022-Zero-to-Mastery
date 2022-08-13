# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {'name': 'Sorna','valid': False}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
        return fn(*args, **kwargs)
    else:
         print('You are not authenticated to login')
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)



#understanding how args[1]['valid']/args[0]['valid'] works

user1 = {
    'name': 'Sorna',
    'valid': True
}
user2 = {
    'name': 'User2',
    'valid': False
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[1]['valid']:
          return fn(*args, **kwargs)
        else:
          print('not allowed')
    return wrapper

@authenticated
def message_friends(user, user_two):  #here (args[0] is user) & (args[1] is user_two)
    print('message has been sent')

message_friends(user2, user1)    
message_friends(user1, user2) 