new_list = [1,2,3]
old_list = [5,6,7]

x = zip(new_list,old_list)
print (list(x))

#OR

print (list(zip(new_list,old_list)))




a = [1,2,3,4]
b = [5,6]
c = [7,8,9,10,11]

print (list(zip(a,b,c)))



#The zip() function returns a zip object, which is an iterator of tuples where
#the first item in each passed iterator is paired together, and then the second
#item in each passed iterator are paired together etc.

#If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.