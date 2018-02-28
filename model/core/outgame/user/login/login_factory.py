from model.core.outgame.user.login.login_object import Login


class LoginFactory(object):
	"""
	Login factory object
	"""
	def get_object(self):
		return Login()
