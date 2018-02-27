from model.core.outgame.user.auth.token.token_auth_object import TokenAuthentication


class TokenAuthenticationFactory(object):
	"""
	Token authentication factory object
	"""
	def get_object(self):
		return TokenAuthentication()
