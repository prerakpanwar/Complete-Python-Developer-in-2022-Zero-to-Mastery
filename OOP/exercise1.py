#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1= Cat('black',10)
cat2= Cat('brown',5)
cat3= Cat('white',8)

# 2 Create a function that finds the oldest cat

def oldestcat(*args):
  return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldestcat(cat1.age, cat2.age, cat3.age)} years old.")

#OR

# all_cats_age = [cat1.age, cat2.age, cat3.age]

# def OldestCat(): 
#     return max(all_cats_age)

# print(f'the oldest cat is {OldestCat()} years old')