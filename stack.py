stack=[]

def push():
    element=input("Enter element to push:")
    stack.append(element)
    print(f"{element} is pushed into the stack:")

def pop():
    if not stack:
        print("stack is empty.nothing to pop.")

    else:
         
         popped=stack.pop()
         print(f"popped element:{popped}")
         
def display():
    if not stack:
        print("stack is empty.")
    else:
        print("stack element:",stack)


while True:
    print("options:1.push  2.pop  3.Display  4.exit")
    a=input("enter your choice(1/2/3/4):")
    if a =='1':
         push()

    elif a   =='2':
          
          pop()

    elif a=='3':
          display()
    elif a=='4':
          print("Exiting program.")
          break
    else:
           print("Invalid choice.try agin.")

