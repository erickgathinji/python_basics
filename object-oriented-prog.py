#cylinder
import math


class Cylinder:
    def __init__(self,radius,height, color):
        self.r = radius
        self.h = height
        self.rangi = color

    def calc_area(self, is_closed = True): #made it dynamic - either closed or open
        if is_closed:
            area = 2 * math.pi * self.r **2 + 2 * math.pi * self.r * self.h
            print(f"Area of closed cylinder is: {area}")
        else:
            area = math.pi * self.r ** 2 + 2 * math.pi * self.r * self.h
            print(f"Area of open cylinder is: {area}")

    def calc_volume (self):
        v = math.pi * self.r ** 2 * self.h
        print(f"Volume of cylinder is: {v}")

#Don't quote the measurements
c1 = Cylinder (10, 11, "red")
c2 = Cylinder (7.8, 22.6, "blue")
c1.calc_volume()
c1.calc_area(is_closed=False)
c1.calc_area()

