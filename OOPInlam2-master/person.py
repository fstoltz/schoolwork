

class Person:

	def setAddress(self, address):
		"""
		Checks that the address is of type string before setting it
		"""
		if isinstance(address, str):
			self._address = address
		else:
			self._address = None

	def __init__(self, initialName, initialAddress):
		self._name = initialName
		self._address = None
		self.setAddress(initialAddress)


	def getAddress(self):
		"""
		Returns the address of the object
		"""
		return self._address

	def getName(self):
		"""
		Returns the name of the object
		"""
		return self._name

	def __str__(self):
		"""
		Specifies how a str(myObject) call should be interpreted
		"""
		return "Person[name={name},address={address}]"\
		        .format(name=self.getName(), address=self.getAddress())



