#!/usr/bin/python3
"""First Rectangle
"""


from models.base import Base


class Rectangle(Base):
    '''
        class Rectangle that inherits from Base
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            Class constructor
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.setter_checker("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.setter_checker("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.setter_checker("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.setter_checker("y", value)
        self.__y = value

    @staticmethod
    def setter_checker(attr, val):
        if type(val) != int:
            raise TypeError("{} must be an integer".format(attr))
        if attr == "x" or attr == "y":
            if val < 0:
                raise ValueError("{} must be >= 0".format(attr))
        elif val <= 0:
            raise ValueError("{} must be > 0".format(attr))

    def area(self):
        '''
            returns the area value of the Rectangle instance
        '''
        return (self.height * self.width)

    def display(self):
        '''
            prints in stdout the Rectangle instance with the character #
        '''
        rec = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rec += (" " * self.x) + ("#" * self.width) + "\n"
        print(rec, end="")

    def __str__(self):
        '''
            returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        '''
            assigns an argument to each attribute
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
