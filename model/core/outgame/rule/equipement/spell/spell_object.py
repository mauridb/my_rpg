import uuid
import random


class Spell(object):
	"""
	Spell object to extend
	"""
	def __init__(self, spell_type=None):
		self.spell_type = spell_type

	def __str__(self):
		return str(self.spell_type)

	def get_object_id(self):
		return str(uuid.uuid1())


class Fire(Spell):
	"""
	Fire spell object
	"""
	def __init__(self, damage_type='burn'):
		self.damage_type = damage_type
		self.damage = random.randint(0, 100)

	def __str__(self):
		return 'Fire'


class Water(Spell):
	"""
	Water spell object
	"""
	def __init__(self, damage_type=None):
		self.damage_type = damage_type
		self.damage = random.randint(0, 100)

	def __str__(self):
		return 'Water'


class Wind(Spell):
	"""
	Wind spell object
	"""
	def __init__(self, damage_type=None):
		self.damage_type = damage_type
		self.damage = random.randint(0, 100)

	def __str__(self):
		return 'Wind'


class Earth(Spell):
	"""
	Earth spell object
	"""
	def __init__(self, damage_type=None):
		self.damage_type = damage_type
		self.damage = random.randint(0, 100)

	def __str__(self):
		return 'Earth'
