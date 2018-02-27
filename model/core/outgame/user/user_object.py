import uuid


class User(object):
	"""
	User object
	"""
	def __init__(self, first_name=None, last_name=None):
		self.__first_name = first_name
		self.__last_name = last_name

	def get_full_name(self):
		return '%s %s' % (self.__first_name, self.__last_name)

	def get_object_id(self):
		return str(uuid.uuid1())

	def __str__(self):
		return 'User: %s' % (self.get_full_name())
