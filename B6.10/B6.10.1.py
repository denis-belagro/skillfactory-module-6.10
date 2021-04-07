class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_str_rectangle(self):
        return  self.x, self.y, self.width, self.height

p1 = Rectangle(5, 10, 50, 100)

print("Rectangle", str(p1.get_str_rectangle()))