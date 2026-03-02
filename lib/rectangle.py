from lib.shape import Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width < 5:
            return 2 * (self.width + self.height)
        elif self.width > 6:
            return 2 * (self.width + self.height)

        return 2 * (self.width + self.height)
