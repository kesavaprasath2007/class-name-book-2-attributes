import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    

    def area(self):
         area=math.pi*self.radius**2
         print("area:",area)
    def  circumference(self):
          circumference=2*math.pi*self.radius
          print("circumference:",circumference)
          
        

a=int(input("Enter the radius"))
r=circle(a)
r.area()
r.circumference()

          

