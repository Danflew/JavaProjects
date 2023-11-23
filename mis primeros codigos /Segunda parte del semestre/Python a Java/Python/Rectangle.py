class Rectangle:
    def __init__(self, length, width):
        print("Creating rectangle with length {l} and width {w}".format(l=length, w=width))
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

paper = Rectangle(8, 11)  # Assuming standard letter-sized paper with 8x11 inches
keyboard = Rectangle(18, 6)  # Typical keyboard dimensions
smartphone = Rectangle(5.7, 2.8)  # Example smartphone dimensions

print("Perimeter of Smartphone:", smartphone.perimeter())
print("Area of Smartphone:", smartphone.area())
print("Perimeter of Keyboard:", keyboard.perimeter())
print("Area of keyboard:", keyboard.area())
print("Perimeter of paper:", paper.perimeter())
print("Area of paper:", paper.area())

