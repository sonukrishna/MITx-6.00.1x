def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    notGuessed = []
    for i in range(26):
        notGuessed += chr(i + ord('a'))
    for j in lettersGuessed:
        notGuessed.remove(j)
    string = ''
    for k in notGuessed:
        string += k
    return string


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)
