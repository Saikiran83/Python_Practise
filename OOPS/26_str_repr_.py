# This method returns the string representation of the object. This method is called when print() or str() function is invoked on an object. This method must return the String object. If we don’t implement __str__() function for a class, then built-in object implementation is used that actually calls __repr__() function.
# Python __repr__() function returns the object representation in string format. This method is called when repr() function is invoked on the object. If possible, the string returned should be a valid Python expression that can be used to reconstruct the object again
# the __str__ function is supposed to return a human-readable format, which is good for logging or to display some information about the object. Whereas, the __repr__ function is supposed to return an “official” string representation of the object, which can be used to construct the object again.
import datetime
now = datetime.datetime.now()
print(now.__str__()) # '2020-12-27 22:28:00.324317'

print(now.__repr__()) # 'datetime.datetime(2020, 12, 27, 22, 28, 0, 324317)'

# It’s clear from the output that __str__() is more human friendly whereas __repr__() is more information rich and machine friendly and can be used to reconstruct the object. In fact, we can use repr() function with eval() to construct the object.

now1 = eval(repr(now))
print(now == now1)

#####################

class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def __str__(self):
        return f'Person name is {self.name} and age is {self.age}'

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


p = Person('Pankaj', 34)

print(p.__str__())
print(p.__repr__())

# Earlier we mentioned that if we don’t implement __str__ function then the __repr__ function is called. Just comment the __str__ function implementation from the Person class and print(p) will print {name:Pankaj, age:34}.