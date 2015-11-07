
def oddTuple(tup):
    rtup = ()
    for i in range(len(tup)):
	if i%2 == 0:
	    rtup += (tup[i],)
    return rtup
print oddTuple(('I', 'am', 'a', 'test', 'tuple'))
