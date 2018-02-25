import uuid

from model.core.outgame.rule.character.character_object import Character


class Enemy(Character):
	"""
	Enemy class object
	"""
	def __init__(self, race=None, char_class=None):
		super().__init__(race, char_class)

	def __str__(self):
		return 'Enemy'

	def get_object_id(self):
		return str(uuid.uuid1())
