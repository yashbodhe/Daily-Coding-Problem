def largestSum(a):
    incl,excl=0,0
    for x in a:
        new_excl=max(incl,excl)
        incl=excl+x
        excl=new_excl
    return max(incl,excl)
    
print(largestSum([2, 4, 6, 8]))
print(largestSum([5, 1, 1, 5]))