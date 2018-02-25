import uuid


class Ingame(object):
	"""
	Ingame object
	"""

	def get_object_id(self):
		return str(uuid.uuid1())


	def __str__(self):
		return 'InGame'

class Outgame(object):
	"""
	Outgame object
	"""

	def get_object_id(self):
		return str(uuid.uuid1())


	def __str__(self):
		return 'OutGame'