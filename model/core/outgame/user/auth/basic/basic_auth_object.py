from model.core.outgame.user.auth.authentication_object import Authentication


class BasicAuthentication(Authentication):
	"""
	Basic authentication object
	"""
	def __init__(self, username=None, password=None):
		self.username = username
		self.password = password

	def __str__(self):
		return 'BasicAuthentication'		
