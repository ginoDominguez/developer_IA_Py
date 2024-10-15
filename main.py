### Sample od Use OOP:

class Square:
      def __init__(self):
          self.__height = 2
          self.__width = 2
def set_side(self, new_side):
          self.__height = new_side
          self.__width = new_side

@property
def get_height(self):
    return self.__height

@height.setter
def set_height(self, h):
    if h>= 0 :
        self.__height = h
    else:
        raise Exception("Ingresar un valor mayorn a cero")


square = Square()
square.__height = 3 # raises AttributeError

print(square.__height)
