import uuid


class Authentication(object):
	"""
	Authentication object
	"""
	def __init__(self, auth_type=None):
		self.auth_type = auth_type

	def get_object_auth(self):
		return self.auth_type.__dict__

	def get_object_id(self):
		return str(uuid.uuid1())

	def __str__(self):
		return str(self.auth_type)
