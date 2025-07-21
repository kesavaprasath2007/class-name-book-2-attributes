class Book:
    def __init__(self,title,author):
    
          self.title=title
          self.author=author

    def display(self):
         
         print("title:",self.title)
         print("author:",self.author)

b1=Book("The Alchemist","Paulo Coelho")
b1.display()
