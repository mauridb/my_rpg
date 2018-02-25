from model.core.game_object import Ingame, Outgame


class IngameFactory(object):
	"""
	Ingame Factory 
	"""

	def get_object(self):
		return Ingame()

class OutgameFactory(object):
	"""
	Outgame Factory 
	"""

	def get_object(self):
		return Outgame()