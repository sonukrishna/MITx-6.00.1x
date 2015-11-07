def count7(n):
    if n < 7:
        break
    count = 0
    if n == 7:
	count += 1
	return count
    return count7(n/10)

print count7(777)
