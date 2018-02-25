import uuid


class Dice(object):
	"""
	Dice object to extend
	"""

	def __init__(self, size=None):
		self.size = size

	def __str__(self):
		return 'D'+str(self.size)


class D4(Dice):
	"""
	Dice 4 
	"""

	def __init__(self, size=4):
		super().__init__(size)

	def __str__(self):
		return super().__str__()

	def get_object_id(self):
		return str(uuid.uuid1())


class D6(Dice):
	"""
	Dice 6 
	"""

	def __init__(self, size=6):
		super().__init__(size)

	def __str__(self):
		return super().__str__()

	def get_object_id(self):
		return str(uuid.uuid1())


class D8(Dice):
	"""
	Dice 4 
	"""

	def __init__(self, size=8):
		super().__init__(size)

	def __str__(self):
		return super().__str__()

	def get_object_id(self):
		return str(uuid.uuid1())


class D10(Dice):
	"""
	Dice 10 
	"""

	def __init__(self, size=10):
		super().__init__(size)

	def __str__(self):
		return super().__str__()

	def get_object_id(self):
		return str(uuid.uuid1())


class D12(Dice):
	"""
	Dice 12 
	"""

	def __init__(self, size=12):
		super().__init__(size)

	def __str__(self):
		return super().__str__()

	def get_object_id(self):
		return str(uuid.uuid1())


class D20(Dice):
	"""
	Dice 20 
	"""

	def __init__(self, size=20):
		super().__init__(size)

	def __str__(self):
		return super().__str__()

	def get_object_id(self):
		return str(uuid.uuid1())


class DRate(Dice):
	"""
	Dice rate percent [00, 10, 20.. 90]
	"""

	def __init__(self, size=10):
		super().__init__(size)

	def __str__(self):
		return super().__str__()

	def get_object_id(self):
		return str(uuid.uuid1())
