def sum_two_numbers(l1,l2):
    n1=int("".join(map(str,l1[::-1])))
    n2=int("".join(map(str,l2[::-1])))
    a=n1+n2
    return[int(x) for x in str(a)[::-1]]

l1=list(map(int,input('l1:').split()))
l2=list(map(int,input('l2:').split()))


result=sum_two_numbers(l1,l2)
print('output:',result)


        
