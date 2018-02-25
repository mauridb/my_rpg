from model.core.outgame.rule.enemy.boss.boss_object import Boss
from model.core.outgame.rule.character.character_factory import get_race, get_class


class BossFactory(object):
	"""
	Boss factory object
	"""
	def get_object(self):
		return Boss(get_race(), get_class())
