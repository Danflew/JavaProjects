class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        self.radius = diameter / 2

    def circumference(self):
        return 2 * self.pi * self.radius

    def area(self):
        return self.pi * self.radius**2

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print("Circumference of medium pizza:", medium_pizza.circumference())
print("Area of medium pizza:", medium_pizza.area())
print("Circumference of teaching table:", teaching_table.circumference())
print("Area of teaching table:", teaching_table.area())
print("Circumference of round room:", round_room.circumference())
print("Area of round room:", round_room.area())
