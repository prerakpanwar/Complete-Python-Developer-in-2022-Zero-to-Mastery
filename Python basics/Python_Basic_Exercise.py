#1-Use a multiline string to make the a multi line comment:

'''
This is a comment
written in 
more that just one line
'''

#2-Get the first character of the string txt.

txt = "Hello World"
x = txt[0]

#3-Get the characters from index 2 to index 4 (llo).

txt = "Hello World"
x = txt[2:5]

#4-Return the string without any whitespace at the beginning or the end.

txt = " Hello World "
x = txt.strip()

#5-Replace the character H with a J.

txt = "Hello World"
txt = txt.replace("H", "J") 

#6-Insert the correct syntax to add a placeholder for the age parameter.

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#7-Use the correct membership operator to check if "apple" is present in the fruits object.

fruits = ["apple", "banana"]
if "apple" in fruits:
	print("Yes, apple is a fruit!")

#8-Print the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#9-Change the value from "apple" to "kiwi", in the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#10-Use the insert method to add "lemon" as the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#11-Use negative indexing to print the last item in the list.

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#12-Use the correct syntax to print the number of items in the list.

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#13-Use the correct method to add multiple items (more_fruits) to the fruits set.

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#14-Change the "year" value from 1964 to 2020.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020 			#OR car.update({'year': 2020})
print(car)

#15-Add the key/value pair "color" : "red" to the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"
print(car)

#16-Use the correct short hand syntax to write the following conditional expression in one line:

# if 5 > 2:
#   print("Yes")
# else
#   print("No")

print('yes') if 5>2 else print('no')

#17-Print a message once the condition is false.

i = 1
while i < 6:
  print(i)
  i += 1
else:
	print("i is no longer less than 6")

#18-In the loop, when the item value is "banana", jump directly to the next item.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

























