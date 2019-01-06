class Employe:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
		self.email = fname + '@' + lname + '.com'

	def showfullDetails(self):
		print(self.fname + ' ' + self.lname + ' ' + self.email)

emp1 = Employe('test1', 'test2')

print(emp1.email)
emp1.showfullDetails()		  # the class have already instance
Employe.showfullDetails(emp1) # call method whith emp1 instance



