# The abstract classes may also contain concrete methods that have the implementation of the method and can be used by all the concrete classes. To define a concrete method in an abstract class, we simply define a method with implementation and don’t decorate it with the @abstractmethod decorator. If needed, we may also override this concrete method in the concrete class to provide any additional functionality as per user needs.

from abc import ABC, abstractmethod, abstractproperty
 
class Shape(ABC):
    def __init__(self, shape_name):
        self.shape_name = shape_name
 
    def print_greetings(self):
        print("Hello from Shape class")
     
    @abstractmethod
    def draw(self):
        pass
class Circle(Shape):
    def __init__(self):
        super().__init__("circle")
 
    def draw(self):
        super().draw()
        print("Drawing a Circle")
#create a circle object
circle = Circle()
circle.print_greetings()