class Triangle:
    def __init__(self, side1, side2, side3):
        print("Creating a triangle with sides {s1}, {s2}, and {s3}".format(s1=side1, s2=side2, s3=side3))
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.perimeter() / 2  # Semiperimeter
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

slice_of_pizza = Triangle(8, 8, 8)  # Assuming an equilateral triangle
emergency_symbol = Triangle(3, 4, 5)  # A right triangle
ice_cream_cone = Triangle(5, 12, 13)  # Another right triangle

print("Perimeter of a slice of pizza:", slice_of_pizza.perimeter())
print("Area of a slice of pizza:", slice_of_pizza.area())

print("Perimeter of an emergency symbol:", emergency_symbol.perimeter())
print("Area of an emergency symbol:", emergency_symbol.area())

print("Perimeter of an ice cream cone:", ice_cream_cone.perimeter())
print("Area of an ice cream cone:", ice_cream_cone.area())
