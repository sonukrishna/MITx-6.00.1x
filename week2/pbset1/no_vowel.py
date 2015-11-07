

def count_vowel(s):
    """this function counts the no.of vowels in s """
    count = 0
    for i in s:
	if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
	    count += 1
    print "Number of vowels:%d" %count

#s = "what the difference between engineer and a common man"
count_vowel(s)
