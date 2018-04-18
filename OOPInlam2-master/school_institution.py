from school import School



class NotEnoughMoney(BaseException):
	pass

#Could not name it to __SchoolInstitution, introduces NameError
#during testing in main.py
class SchoolInstitution: # <---- Singleton!
	def __init__(self):
		self.name = "Skolverket"
		self._schools = []

	def addSchool(self, schoolObj):
		"""
		para 1: a School object
		Returns None
		"""
		self._schools.append(schoolObj)

	def createNewSchool(self):
		print("\nName of School to Register: ", end="")
		newS = School( str(input()) )
		self.addSchool(newS)
		print("\nSuccessfully registered new school: {}\n".format(newS.getSchoolName()))

	def displayAllSchools(self):
		print("\n\t    NAME    |  ACTIVE")
		for school in self._schools:
			print("\t{schoolName}".format(schoolName=school.getSchoolName()) + "-"*5, end="")
			print("{status}".format(status=school.getStatus()), end="\n")
		print("\n")

	def takeTaxMoney(self, schoolObj):
		"""
		para 1: a School object
		Requests a tax sheet from the school
		"""
		try:
			if schoolObj.getStatus() == True:
				moneyToTax = schoolObj.getTaxSheet()
				print("Taxdeductable transactions: {}".format(moneyToTax))
				moneyToTake = moneyToTax * 0.3
				print("Amount to tax (30%): {}".format(moneyToTake))

				if moneyToTake < schoolObj.getBalance():
					schoolObj._balance -= moneyToTake
				else:
					# School Institution is part of the state and are almighty
					# and have access to schools' bank accounts.
					print("\n\n\t>---- School does not have sufficient funds to pay the tax.\n"\
						"\t\tThe school will be shutdown, effective immediately ----<\n\n")
					raise NotEnoughMoney()

			elif schoolObj.getStatus() == False:
				print("School is not active.")

		except NotEnoughMoney:
			#If the nschool doesn't have enough money to pay the tax,
			#lets shut it down.
			self.terminateSchool(schoolObj)

	def terminateSchool(self, schoolObj):
		"""
		para 1: a School object
		Closes/Terminates the school specified
		"""
		if schoolObj.getStatus() != False:
			print("\nSearching for the school...")
			for school in self._schools:
				if (schoolObj.getSchoolName()) == school.getSchoolName():
					schoolObj._active = False
					print("Successfully terminated school\n") #<- Legally, it's no longer a valid school, 
															  # but it may still operate illegally without paying tax(crime!),
															  # it has not been removed physically
					return
		print("Something unexpected occurred.\n")
		return None

	def giveWarningToSchool(self, schoolObj):
		"""
		para 1: a School object
		Gives a warning to the school
		"""
		#I was thinking here, that the school can make a health survey
		#checkup on a school, and that checkup goes through each
		#student and staff in the school, and then I would add
		#a new attribute to the Person() class, something like
		#"self.mood = Satisfied/Dissatisfied/Unsure.. etc.
		#and based on the results of going through everyones' mood.
		#If the average mood is dissatisfied, issue a warning to the 
		#school. And maybe also start a timer at this point, and say
		#that the date of the timer started plus 60 days, a new checkup
		#should be made from skolverket, and if the average mood is still
		#dissatified, shutdown the school. If average mood is now satisfied,
		#do nothing.
		pass






