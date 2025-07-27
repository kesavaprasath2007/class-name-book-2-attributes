def next_greater_element(arr):
    result=[]
    stack=[]


    for i in range(len(arr)-1,-1,-1):
        current=arr[i]

        while stack and stack[-1]<=current:
            stack.pop()


        if not stack:
            result.insert(0,-1)
        else:
            result.insert(0,stack[-1])


        stack.append(current)

    return result
arr=list(map(int,input("enter number seprated by space:").split()))

print("next_greater_element:",next_greater_element(arr))    
