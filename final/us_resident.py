class Person(object):
    def __init__(self, name):
	#create a person with name name
	self.name = name
	try:
	    firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
	except:
	    self.lastName = name
    def getLastName(self):
	#create self's last name
        return self.lastName
    def setAge(self, age):
        #assume age is an int greater than zero
	#returns self's current age in years
	if self.age == None:
	    raise ValueError
	return self.age
   def __lt__(self, other):
	#return True if self's name  is lexicographically
        #less than other's name, and False otherwise
        if self.lastName == other.lastName:
	    return self.name < other.name
	return self.lastName < other.lastname
    def __str__(self):
	#returns selfs name
	return self.name

class USResident(Person):
    """ a person who resides in the US """
    def __init__(self, name, status):
        Person.__init__(self, name)
        if status in ["citizen", "non-resident"]:
	    self.status = status
       else:
       	    raise ValueError

    def getStatus(self):
	# return status
	return self.status

