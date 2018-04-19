

class Program:
	def __init__(self, name):
		self._programName = name
		self._students = []

	def addStudent(self, studObj):
		self._students.append(studObj)

	def getAllStudentNames(self):
		nameList = []
		for student in self._students:
			nameList.append(student.getName())
		return nameList

	def getName(self):
		return self._programName

	def numberOfStudents(self):
		i = 0
		for student in self._students:
			i += 1
		return i

	def getTotalIncome(self):
		"""'
		Returnera kostnaden för varje student och lägg i en variabel
		"""
		fee = 0
		for student in self._students:
			fee += student.getFee()
		return fee

	def getStudents(self):
		return self._students