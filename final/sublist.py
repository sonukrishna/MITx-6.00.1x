def sublist(L, n):
    res = []
    for i in range(len(L)):
        x = L[i : n + i]
	if len(x) == n:
	    res.append(x)
    return res


L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print sublist(L, 4)
