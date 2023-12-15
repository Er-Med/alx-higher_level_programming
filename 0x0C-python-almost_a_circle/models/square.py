#!/usr/bin/python3
"""
Square module class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that that inherits from Base class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize class constructor.
        Args:
            id      (int): The identity of the new Square.
            size    (int): The size of the new Square.
            x       (int): The x coordinate of the new Square.
            y       (int): The y coordinate of the new Square.
        Raises:
            TypeError    : If either of width or height is not an int.
            ValueError   : If either of width or height <= 0.
            TypeError    : If either of x or y is not an int.
            ValueError   : If either of x or y < 0.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the Square.
        Args:
            1st argument should be the (id)   attribute.
            3rd argument should be the (size) attribute.
            4th argument should be the (x)    attribute.
            5th argument should be the (y)    attribute.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
