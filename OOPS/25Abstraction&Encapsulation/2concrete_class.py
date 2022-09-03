# Unlike some other programming languages, Python abstract methods don’t need to be completely abstract, they can have some basic level implementation that can be used by all the concrete classes. A Concrete class is a class that has a definition for all its methods and has no abstract method.
# Concrete classes can use the super() to call the base abstract method and do some additional tasks into it. In our example, the abstract method draw() of the Shape class could be used to prepare a basic canvas and then concrete classes could work on top of that to draw specific shapes.

from abc import ABC, abstractmethod, abstractproperty
 
class Shape(ABC):
    def __init__(self, shape_name):
        self.shape_name = shape_name
    
    @abstractmethod
    def draw(self):
        print("Preparing the Canvas")

class Circle(Shape):
    def __init__(self):
        super().__init__("circle")
 
    def draw(self):
        super().draw()
        print("Drawing a Circle")
#create a circle object
circle = Circle()
circle.draw()