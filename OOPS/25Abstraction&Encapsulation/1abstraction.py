from abc import ABC, abstractmethod, abstractproperty
 
class Shape(ABC):
    def __init__(self, shape_name):
        self.shape_name = shape_name

    @abstractproperty
    def name(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass
 
class Rectangle(Shape):
    def __init__(self):
        super().__init__("Rectangle")
    @property
    def name(self):
        return self.shape_name
    def draw(self):
        print("Drawing a Rectangle")
 
class Circle(Shape):
    def __init__(self):
        super().__init__("circle")
    @property
    def name(self):
        return self.shape_name
    def draw(self):
        print("Drawing a Circle")

#create a circle object
circle = Circle()
circle.draw()
print(f"The shape name is: {circle.name}")
#create a Rectangle object
Rectangle = Rectangle()
Rectangle.draw()
