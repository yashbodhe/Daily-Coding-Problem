def newArray(a):
    left=[]
    l=1
    for x in a:
        left.append(l)
        l*=x
    right=[]
    r=1
    for x in a[::-1]:
        right.append(r)
        r*=x    
    right=right[::-1]
    res=[]
    for i in range(len(a)):
        res.append(left[i]*right[i])
    return res
    

print(newArray([1,2,3,4,5]))
print(newArray([3, 2, 1]))