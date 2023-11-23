class Square:
    def __init__(self, side_length):
        print("Creating square with side length {s}".format(s=side_length))
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

    def area(self):
        return self.side_length ** 2

Laptop = Square(5)
Tower = Square(8)
Box= Square(12)

print("Perimeter Tower", Tower.perimeter())
print("Area of Tower", Tower.area())
print("Perimeter Box", Box.perimeter())
print("Area of Box", Box.area())
print("Perimeter Laptop", Laptop.perimeter())
print("Area of Laptop", Laptop.area())
