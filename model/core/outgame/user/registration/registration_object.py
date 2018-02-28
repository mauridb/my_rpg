import uuid


class Registration(object):
	"""
	Registration object
	"""
	def __init__(self, username=None, password=None):
		self.username = username
		self.password = password

	def get_object_id(self):
		return str(uuid.uuid1())

	def __str__(self):
		return 'Registration'
