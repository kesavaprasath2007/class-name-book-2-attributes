class employee():
    def __init__(self,name,basic_salary):
        self.name=name
        self.basic_salary=basic_salary
        
    def calculate_hra(self):
         self.hra=0.10*self.basic_salary
         print("HRA:",self.hra)
         
    def calculate_da(self):
          self.da=0.5*self.basic_salary
          print("DA:",self.da)

    def total_salary(self):
           total=self.basic_salary+self.hra+self.da
           print("total:",total)
           
a=input("Enter the your name:")
b=int(input("Enter the basic salary:"))
E=employee(a,b)
E.calculate_hra()
E.calculate_da()
E.total_salary()
