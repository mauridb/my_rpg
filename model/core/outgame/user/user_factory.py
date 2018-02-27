from model.core.outgame.user.user_object import User


class UserFactory(object):
	"""
	User factory object
	"""
	def get_object(self):
		return User(first_name='<<FIRST_NAME>>', last_name='<<LAST_NAME>>')
