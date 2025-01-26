# Abstraction   √ 
# polymorphism  X
# encapsulation √ 
# inheritance   X
import random
class Triangle:
    id = []
    def __init__(self, side_a = 0, side_b = 0, side_c = 0):
        # ID Choosing Section
        id_choose = random.randint(0,1000000)
        if len(Triangle.id)<1000000:
            while id_choose in Triangle.id:
                id_choose = random.randint(0,1000000)
            Triangle.id.append(id_choose)
            self._a = side_a
            self._b = side_b
            self._c = side_c
            self._perimeter = side_a+side_b+side_c
            self.id = id_choose
            print("ID: ",self.id)
            half_peri = self.perimeter()/2
            area = (half_peri*(half_peri-side_a)*(half_peri-side_b)*(half_peri-side_c))**.5
            self._area = area
            if area == 0:
                print(f"No Valid measurements are Given for the object")
                print("===============================\n")
                del self
                # You can commented out the line below, if you are serious
                # raise ValueError("Addition of two sides must be greater than the remaining side...")
        else:
            print("Limit Finished")
            del self
            raise SystemError("Limit exceeded...")

    def perimeter (self):
        return self._perimeter
    
    def area(self):
        return self._area
    
    def __str__(self):
        return f"""The area and perimeter of the triangle is:
        {self.area()} and {self.perimeter()}"""
    
    def __repr__(self):
        return f"This is a triangle object, ID:{self.id}"
    
    def __eq__(self, other):
        try:
            if  self.area() == other.area()\
                and\
                self.perimeter() == other.perimeter():
                return True
            return False
        except:
            return "You need to make an object son"

    def __lt__(self, other):
        try:
            if self.area()<other.area():
                return True
            else:
                return False
        except:
            return "You need to make an object son"



#Driver Script to Understand what's written over
#As this is not taking any input, there will be terminal error for error handling
sq1 = Triangle(15,25,35)
print(sq1)
print(sq1.perimeter())
print(sq1.area())
print("#######################################")
sq2 = Triangle(10,20,30)
print("#######################################")
sq3 = Triangle(40,60,40)
print(sq3)
print(sq3.perimeter())
print(sq3.area())
print("#######################################")
sq4 = Triangle(40,60,56)
print(sq4)
print(sq4.perimeter())
print(sq4.area())
print("#######################################")
sq5 = Triangle(40,40,40)
print(sq5)
print(sq5.perimeter())
print(sq5.area())
print("#######################################")
sq6 = Triangle(1,1,1)
print(sq6)
print(sq6.perimeter())
print(sq6.area())
print("#######################################")
print(sq6==sq1)
print("#######################################")
print(sq6==100)