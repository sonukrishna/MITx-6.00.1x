
def mCount(L):
    count=1

    maxCount=0
    for i in range(len(L)-1):
        if L[i+1] >= L[i]:
            count +=1
        else:

            count =1
        if maxCount<count:
            maxCount=count
    return maxCount

print mCount([10, 4, 6, 8, 3, 4, 5, 7, 7, 2])
