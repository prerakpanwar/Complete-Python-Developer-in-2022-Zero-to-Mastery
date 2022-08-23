import re

string = 'search this inside of this string please'

# print('this' in string)   #using normal search

a= re.search('this', string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())



pattern = re.compile('this')        #we can use pattern everywhere now
string = 'search this inside of this string please'

a= pattern.search(string)
b= pattern.findall(string)
c= pattern.fullmatch(string)       #has to be exact string else it returns none
print(a)
print(b)
print(c)




pattern = re.compile('search this inside of this string please')
pattern2 = re.compile('search this inside of this string pleaseee')
string = 'search this inside of this string please'
string2= 'search this inside of this string pleaseee prerak'
c= pattern.fullmatch(string) 
d= pattern.match(string)
c2=pattern.fullmatch(string2)
d2=pattern.match(string2)        
print(c)
print(d)
print(c2)
print(d2)





