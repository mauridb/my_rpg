from model.core.game_object import Ingame


class IngameFactory(object):
	"""
	Ingame Factory 
	"""

	def get_object(self):
		return Ingame()