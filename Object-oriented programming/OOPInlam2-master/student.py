from person import Person
from datetime import date




class Student( Person ):
	#  Setters 
	def setYear(self, year):
		self._year = year

	def setProgram(self, programPara):
		self._programme = programPara

	def setSchool(self, schoolPara):
		self._school = schoolPara

	def setFee(self, fee):
		self._fee = fee

	#  Constructor 
	def __init__(self, name, address, programme, year, fee, school):

		super().__init__(name, address)

		self._programme = None
		self.setProgram(programme)

		self._year = None
		self.setYear(year)

		self._fee = None
		self.setFee(fee)

		self._school = None
		self.setSchool(school)

	#  Getters
	def getProgram(self):
		"""
		Returns the students program
		"""
		return self._programme

	def getYear(self):
		"""
		Returns the students year
		"""
		return self._year

	def getFee(self):
		"""
		Returns the students fee
		"""
		return self._fee

	# Operators / Helper?

	def __str__(self):
		"""
		Specifies how a str(myObject) call should be interpreted
		"""
		return "Student[Person[name={name},address={address}],program={program},year={year},fee={fee:.2f}]"\
		        .format(name=self.getName(), address=self.getAddress(),\
		        	program=self.getProgram(), year=self.getYear(), fee=self.getFee() )

	def formattedString(self):
		return "\nName: {name}\nAddress: {address}\nProgram: {program}\nYear: {year}\nFee: {fee:.2f}\n"\
		        .format(name=self.getName(), address=self.getAddress(),\
		        	program=self._programme.getName(), year=self.getYear(), fee=self.getFee() )