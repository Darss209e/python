class circle:
    def __init__(self , radius):
        self.radius = radius

    def AREA(self):
        return 3.14*self.radius**2

    def perimeter(self):
        return 2*3.14*self.radius

cir1 = circle(4)
print(cir1.AREA())
print(cir1.perimeter())
        