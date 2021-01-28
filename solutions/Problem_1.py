def findPair(a,k):
    s=set()
    for x in a:
        if k-x in s:
            print(str(x)+" + "+str(k-x)+" = "+str(k),end=" ")
            return True
        s.add(x)
    return False

print(findPair([10, 15, 3, 7],17))
print(findPair([10, 15, 3, 7],18))
print(findPair([10, 15, 3, 7],19))