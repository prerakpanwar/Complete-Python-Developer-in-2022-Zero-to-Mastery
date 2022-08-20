#Useful modules
#1-collections

from collections import Counter,defaultdict,OrderedDict

li = [1,2,3,4,5,6,7,7,5,5]
sentence = 'baa baa black sheep dont have wool'

print(Counter(li))							
print(Counter(sentence))

my_dict = defaultdict(lambda : 'does not exist', {'a':1 ,'b':2}) 		#defaultdict - dict subclass that calls a factory function to supply missing values
print(my_dict['c']) 				#trying to access 'c' which is not in the dict
print(my_dict['a'])

d = OrderedDict()
d['a']=1
d['b']=2

d2 = OrderedDict()
d2['a']=1
d2['b']=2

print(d2 == d)

d = OrderedDict()
d['a']=1
d['b']=2

d2 = OrderedDict()
d2['b']=2
d2['a']=1

print(d2 == d)

#Recently, the Python has made Dictionaries ordered by default! 
#So unless you need to maintain older version of Python (older than 3.7), 
#you no longer need to use ordered dict, you can just use regular dictionaries!

#but with regular dictionary it will be true as all key value pairs are same 
#because dict in python has no sense of order for older versions
d = {'c':3}
d['a']=1
d['b']=2

d2 = {'c':3}
d2['b']=2
d2['a']=1

print(d2 == d)

######################################################################
#2-datetime

import datetime

print(datetime.time())
print(datetime.time(9,58,2))

print(datetime.date.today())

######################################################################
#3-array
#when you have massive list and don't want to use generators the use this
#more performant then list[]

from array import array

arr = array('i', [1,2,3])

print(arr)
print(arr[0])   

