from model.core.outgame.user.auth.basic.basic_auth_object import BasicAuthentication


class BasicAuthenticationFactory(object):
	"""
	Basic factory authentication
	"""
	def get_object(self):
		return BasicAuthentication()
