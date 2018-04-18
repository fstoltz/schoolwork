

class School:
	#Constructor
	def __init__(self, name, bal=5000000, status=True):
		"""
		Initializes with an empty _programs and _staff list
		"""
		self._schoolName = name
		self._programs = []
		self._staff = []
		self._balance = bal
		self._active = status

	def addProgram(self, programObj):
		"""
		Para: programObj
		Object to append to the _programs list
		"""
		self._programs.append(programObj)

	def addStaff(self, staffObj):
		"""
		Para: staffObj
		Object to append to the _staff list
		"""
		self._staff.append(staffObj)

	def getTotalStaffCost(self):
		"""
		Returns the sum of all staffs salaries
		"""
		pay = 0
		for staff in self._staff:
			pay += staff.getPay()
		return pay

	def profit(self):
		"""
		Return the difference between student fees and staff expense
		"""
		studentIncome = 0
		for program in self._programs:
			studentIncome += program.getTotalIncome()

		return studentIncome - self.getTotalStaffCost()

	def getStudentIncome(self):
		studentIncome = 0
		for program in self._programs:
			studentIncome += program.getTotalIncome()
		return studentIncome

	def getPrograms(self):
		"""
		Returns the schools' _programs list attribute
		"""
		return self._programs

	def getProgramsName(self):
		"""
		Returns a string with the name of all the schools' programs
		"""
		programStr = ""
		for program in self._programs:
			programStr += program.getName() + " "
		return programStr

	def getProgramNameAsList(self):
		"""
		Returns the name of all the schools' programs, as elements in a list
		"""
		progrNameLi = []
		for program in self._programs:
			progrNameLi.append(program.getName())
		return progrNameLi

	def getAllStaffName(self):
		"""
		Returns a string containing the name of every staff object in the school
		"""
		staffStr = ""
		for staff in self._staff:
			staffStr += staff.getName() + " "
		return staffStr

	def changeStaffsPay(self, nameOfStaff, newPay):
		"""
		para 1: Name of the staff you wish to change salary for
		para 2: The new salary
		Returns None
		"""
		staffObj = None
		for staff in self._staff:
			if (staff.getName() == nameOfStaff):
				staffObj = staff
				staffObj.setPay(newPay)
				return

	def fireStaff(self, nameOfStaff):
		"""
		para 1: Name of the staff you wish to fire
		Returns None
		"""
		i = 0
		for staff in self._staff:
			if (staff.getName() == nameOfStaff):
				del self._staff[i]
				return
			i += 1

	def expelStudent(self, nameOfStudent):
		"""
		"""
		for program in self._programs:
			i = 0
			for student in program._students:
				if(nameOfStudent == student.getName()):
					program._students.remove(student)
					print("\n\tSuccessfully expelled student.\n")
					return "found" #<--- for testing purposes
				i += 1
		print("\n\tCould not find a student with that name.\n")
		return "Not found" #<--- for testing purposes


	def getTaxSheet(self):
		taxDeductableTransactions = self.getStudentIncome() + self.getTotalStaffCost()
		return taxDeductableTransactions


	def getSchoolName(self):
		"""
		Returns the name of the school
		"""
		return self._schoolName

	def getBalance(self):
		"""
		Returns the balance for the school
		"""
		return self._balance

	def getStatus(self):
		return self._active


	def __str__(self):
		"""
		Specifies how a str(schoolObj) should be handled.
		"""
		if self.getStatus() == True:
			return "School:{schoolName},\nPrograms:{programsNames},\nStaff:{staffsNames},\nSalaries:{staffSalaries},\nProfit:{prof},\nBalance:{bal}"\
			.format(schoolName=self._schoolName, programsNames=self.getProgramsName(), staffsNames=self.getAllStaffName()\
				,prof=self.profit(), staffSalaries=self.getTotalStaffCost(), bal=self.getBalance())
		else:
			return "I'm trashed until further notice."







