#modifying dunder methods for an class object


class Toy:
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age
        self.my_dict = {'name': 'prerak', 'class': 'legend'}

    def __str__(self):
        return f'{self.colour}'

    def __len__(self):
        return 5

    def __call__(self):
        return ('yes?')

    def __getitem__(self, i):
        return self.my_dict[i]


octane = Toy('red', 0)
print(str(octane))
print(octane.__str__())
print(len(octane))
print(octane.__len__())
print(octane())  # () special way to call a function using call
print(octane['class'])