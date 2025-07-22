class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def area(self):

        area=self.width*self.length
        print("area:",area)
        
    def perimeter(self):
        perimeter=2*(self.length+self.width)
        print("perimeter:",perimeter)
        
length=int(input("Enter the rectangle lenght:"))
width=int(input("Enter the rectangle lenght:"))
a=Rectangle(length,width)
a.area()
a.perimeter()

