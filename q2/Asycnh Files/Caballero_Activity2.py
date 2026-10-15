
class Rectangle:
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0

        self.width = width
        self.height = height

    # Getter for width
    @property
    def width(self):
        return self.__width

    # Setter for width
    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            raise ValueError("Width should be greater than 0.")

    # Getter for height
    @property
    def height(self):
        return self.__height

    # Setter for height
    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            raise ValueError("Height should be greater than 0.")


# Example usage
rectangle = Rectangle(10, 5)

print("Width:", rectangle.width)
print("Height:", rectangle.height)


