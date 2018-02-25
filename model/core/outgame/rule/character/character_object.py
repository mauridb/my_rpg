import uuid


class Character(object):
	"""
	Character object
	"""
	def __init__(self, race=None, char_class=None):
		self.race = race
		self.char_class = char_class

	def __str__(self):
		return 'Character'

	def get_object_id(self):
		return str(uuid.uuid1())
