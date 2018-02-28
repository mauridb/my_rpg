from model.core.outgame.user.registration.registration_object import Registration


class RegistrationFactory(object):
	"""
	Registration factory object
	"""
	def get_object(self):
		return Registration()
