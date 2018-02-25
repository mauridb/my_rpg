from model.core.outgame.rule.enemy.enemy_object import Enemy
from model.core.outgame.rule.character.character_factory import get_race, get_class


class EnemyFactory(object):
	"""
	Enemy factory object
	"""
	def get_object(self):
		return Enemy(get_race(), get_class())
