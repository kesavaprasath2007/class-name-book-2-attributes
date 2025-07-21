class mobile:
    def __init__ (self,brand,price):
        self.brand=brand
        self.price=price
        
     
    def display(self):
        print("brand",self.brand)
        print("print",self.price)


b=mobile("samsung","$15000")
b.display()
             
