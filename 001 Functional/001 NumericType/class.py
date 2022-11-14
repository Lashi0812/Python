# %%
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive.")
        self._width = width

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Height must be positive.")
        else:
            self._height = height


# %%
r1 = Rectangle(10, 20)
print(r1)
r2 = Rectangle(11, 10)
print(r1.width)