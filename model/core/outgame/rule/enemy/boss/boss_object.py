import uuid
from model.core.outgame.rule.enemy.enemy_object import Enemy


class Boss(Enemy):
	"""
	Boss enemy object
	"""
	def __init__(self, race=None, char_class=None):
		super().__init__(race, char_class)
		self.grade_challange = None

	def __str__(self):
		return 'Boss'

	def get_object_id(self):
		return str(uuid.uuid1())
