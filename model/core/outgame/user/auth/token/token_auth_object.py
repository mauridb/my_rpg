from model.core.outgame.user.auth.authentication_object import Authentication


class TokenAuthentication(Authentication):
	"""
	Token authentication object
	"""
	def __init__(self, username=None, password=None, token=None):
		self.username = username
		self.password = password
		self.token = token

	def __str__(self):
		return 'Token authentication'
