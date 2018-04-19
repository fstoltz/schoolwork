
from person import Person
from school import School

class Staff( Person ):

	def setSchool(self, school):
		"""
		para 1(string): Name of the school that the staff should be assigned to
		"""
		if isinstance(school, str):
			self._school = school
		else:
			self._school = None

	def setPay(self, pay):
		"""
		para 1: The staffs' pay
		"""
		if pay > 0.0:
			self._pay = float(pay)
		else:
			self._pay = None


	def __init__(self, name, address, school, pay):
		super().__init__(name, address)
		self._school = None
		self.setSchool(school)
		self._pay = None
		self.setPay(pay)

	def getPay(self):
		"""
		Returns the pay for the staff obj
		"""
		return self._pay

	def getSchool(self):
		"""
		Returns the school name that the staff is assigned to
		"""
		return self._school

	def __str__(self):
		"""
		Specifies how a str(myObject) call should be interpreted
		"""
		return "Staff[Person[name={name},address={address}],school={school},pay={pay:.2f}]"\
		        .format(name=self.getName(), address=self.getAddress(),\
		        	school=self.getSchool(), pay=self.getPay() )




