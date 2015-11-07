def longest_run(L):
    """This function returns the 
       length of the longest run 
       of monotonically increasing 
       numbers occurring in  
    """
    count = 1
    total_count =0 
    for i in range(len(L)-1):
	if L[i+1] >=L[i]:
	    count += 1
	else:
	    count = 1
	if total_count < count:
	    total_count = count
    return total_count


L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print longest_run(L)
