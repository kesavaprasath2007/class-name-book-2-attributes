class student:
    def __init__ (self,name,mark):
        self.name = name
        self.mark  = mark

    def greet(self):
         if self.mark>=50:
             print(self.name,"has passed")
         else:
             print(self.name,"has failed")
             
a=student("kesava",40)
a.greet()
