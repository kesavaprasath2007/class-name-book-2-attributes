def reverse_string(str):
    stack=[]

    for char in str:
        stack.append(char)


    reversed_str=""

    while stack:
        reversed_str+=stack.pop()


    return reversed_str
    


original = input("Enter a string to reverse:")
reversed_out=reverse_string(original)

print("original string:",original)
print("reversed string:",reversed_out)
