

def alpha_order(s):
    """longest substring of s in alphabetical order """
    first = 0
    last = 0
    temp = 0
    for i in range(1,len(s)):
	if s[i-1] > s[i]:
	    temp = i
	if i-temp > last-first:
	    first = temp
	    last = i
    print "Longest substring in alphabetical order is:%s" %s[first:last+1]
s="aaafjckjkjjckjkdiuckajkckjaiwnxnjkascascsj"
alpha_order(s)
