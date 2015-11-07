
def count_bob(s):
    """this counts the no.of bobs in the string s """
    count = 0
    for i in range(len(s)):
	if s[i] == "b" and not i >= (len(s)-2):
	    if s[i+1] == "o":
		if s[i+2] == "b":
    		    count += 1
    print "Number of times bob occurs is: %d" %count
s = 'bobdjklbobkksdjjdboboosbbbbbob'
count_bob(s)
