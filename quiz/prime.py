def primesList(N):
    '''
    N: an integer
    '''
    # Your code here
    res = [2]
    for num in range(2,N+1):
        prime = True
        for i in range(2, num):
            if (num%i==0):
                prime = False
        if prime:
	   if num not in res:
               res.append(num)
            
    return res
print primesList(196)
