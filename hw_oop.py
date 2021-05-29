from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color = 'Black'):
        self._color = color
        self.area = 0


    def __add__(self,other):
        if self.area != 0 and other.area != 0:
            return self.area + other.area
        
        else:
            self.calculate_area()
            other.calculate_area()
            return self.area + other.area

    def __sub__(self, other):
        if self.area == 0 or other.area == 0:
            self.calculate_area()
            other.calculate_area()
            return self.area - other.area
        else:
            if self.area >= other.area:
                return self.area - other.area
            else:
                raise ArithmeticError


    def __eq__(self,other):
        if self.area == 0 or other.area ==0:
            self.calculate_area()
            other.calculate_area()
            return self.area == other.area
        else:
            return self.area == other.area

    def color(self):
        return self._color

    @abstractmethod
    def calculate_area(self):
        pass
class Circla(Shape):
    def __init__(self,radius, color = 'Black'):
        super().__init__(color)
        self.radius = radius
        self._color = color

    def calculate_area(self):
        pi =3.14
        self.area = pi * self.radius ** 2


class Ractangle(Shape):
    def __init__(self, lenght,height,color='Black',):
        super().__init__(color=color)
        self.lenght = lenght
        self.height = height
        self._color = color

    def calculate_area(self):
        self.area = self.height * self.lenght


class Triangle(Shape):
    def __init__(self,lenght, height, color='Black'):
        super().__init__(color=color)
        self.lenght = lenght
        self.height = height
        self._color = color
    
    def calculate_area(self):
        self.area = self.height * self.lenght /2
        


rectangle = Ractangle(3,4)
rectangle2 = Ractangle(4,3)
triangle = Triangle(5,6,'Red')
circle = Circla(15)
print(f'{triangle + rectangle}')
print(f'{triangle - rectangle}')
print(f'{triangle == rectangle}')
print(f'{rectangle2 == rectangle}')

   





