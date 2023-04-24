#!/usr/bin/python3
"""Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        class Square that inherits from Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
            Class constructor
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        '''
            assigns attributes
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
