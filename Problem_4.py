def findMissingEle(a):
    s,c=0,0
    for x in a:
        if x>0:
            c+=1
            s+=x
    c+=1
    summ=(c*(c+1)//2)
    return summ-s
    

print(findMissingEle([1,2,3,4,5]))
print(findMissingEle([3, 4, -1, 1]))
print(findMissingEle([1, 2, 0]))