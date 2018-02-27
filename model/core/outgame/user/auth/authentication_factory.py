import random

from model.core.outgame.user.auth.authentication_object import Authentication
from model.core.outgame.user.auth.basic.basic_auth_factory import BasicAuthenticationFactory
from model.core.outgame.user.auth.token.token_auth_factory import TokenAuthenticationFactory


def get_auth():
	return random.choice([
		BasicAuthenticationFactory(),
		TokenAuthenticationFactory()
		])

class AuthenticationFactory(object):
	"""
	Authentication factory object
	"""
	def get_object(self):
		return Authentication(auth_type=get_auth().get_object())
