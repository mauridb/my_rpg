import uuid

from model.core.outgame.story.story_object import Story


class Dungeon(Story):
	"""
	Dungeon story object
	"""

	def __init__(self, d_level=None):	
		self.d_level = d_level

	def get_object_id(self):
		return str(uuid.uuid1())

	def __str__(self):
		return str(self.d_level)


class NormalDungeon(Dungeon):
	"""
	Normal dungeon object
	"""
	def __init__(self):
		self.monster_health = 1		
		self.monster_damage = 1
		self.exp = 0

	def __str__(self):
		return 'NormalDungeon'	


class HardDungeon(Dungeon):
	"""
	Hard dungeon object
	"""
	def __init__(self):
		self.monster_health = 2		
		self.monster_damage = 1.3
		self.exp = 0.75

	def __str__(self):
		return 'HardDungeon'	


class ExpertDungeon(Dungeon):
	"""
	Expert dungeon object
	"""
	def __init__(self):
		self.monster_health = 3.2	
		self.monster_damage = 1.89
		self.exp = 1

	def __str__(self):
		return 'ExpertDungeon'	


class MasterDungeon(Dungeon):
	"""
	Master dungeon object
	"""
	def __init__(self):
		self.monster_health = 5.12
		self.monster_damage = 2.73
		self.exp = 2

	def __str__(self):
		return 'MasterDungeon'	


class TormentOneDungeon(Dungeon):
	"""
	TormentOne dungeon object
	"""
	def __init__(self):
		self.monster_health = 8.19		
		self.monster_damage = 3.96
		self.exp = 3

	def __str__(self):
		return 'TormentOneDungeon'	


class TormentTwoDungeon(Dungeon):
	"""
	TormentTwo dungeon object
	"""
	def __init__(self):
		self.monster_health = 13.11		
		self.monster_damage = 5.75
		self.exp = 4

	def __str__(self):
		return 'TormentTwoDungeon'	


class TormentThreeDungeon(Dungeon):
	"""
	TormentThree dungeon object
	"""
	def __init__(self):
		self.monster_health = 20.97	
		self.monster_damage = 8.33
		self.exp = 5.5

	def __str__(self):
		return 'TormentThreeDungeon'	
