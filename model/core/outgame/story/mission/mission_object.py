import uuid

from model.core.outgame.story.story_object import Story


class Mission(Story):
	"""
	Story object 
	"""

	def __init__(self, grade=None):
		self.grade = grade

	def get_object_id(self):
		return str(uuid.uuid1())

	def __str__(self):
		return str(self.grade)


class E(Mission):
	"""
	E-Mission object
	"""
	def __init__(self):
		pass

	def __str__(self):
		return 'E'


class D(Mission):
	"""
	D-Mission object
	"""
	def __init__(self):
		pass

	def __str__(self):
		return 'D'


class C(Mission):
	"""
	C-Mission object
	"""
	def __init__(self):
		pass

	def __str__(self):
		return 'C'


class B(Mission):
	"""
	B-Mission object
	"""
	def __init__(self):
		pass

	def __str__(self):
		return 'B'


class A(Mission):
	"""
	A-Mission object
	"""
	def __init__(self):
		pass

	def __str__(self):
		return 'A'


class S(Mission):
	"""
	S-Mission object
	"""
	def __init__(self):
		pass

	def __str__(self):
		return 'S'


class SS(Mission):
	"""
	SS-Mission object
	"""
	def __init__(self):
		pass

	def __str__(self):
		return 'SS'


class Legend(Mission):
	"""
	Legend-Mission object
	"""
	def __init__(self):
		pass

	def __str__(self):
		return 'Legend'
