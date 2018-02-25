import random

from model.core.outgame.rule.equipement.equipement_object import Equipement


class Potion(Equipement):
	"""
	Potion object
	"""
	def __init__(self, restore=None):
		self.restore = restore

	def __str__(self):
		return 'Potion'


class Rope(Equipement):
	"""
	Rope object
	"""
	def __init__(self, restore=None):
		self.restore = restore

	def __str__(self):
		return 'Rope'


class Stone(Equipement):
	"""
	Stone object
	"""
	def __init__(self, restore=None):
		self.restore = restore

	def __str__(self):
		return 'Stone'


class Torch(Equipement):
	"""
	Torch object
	"""
	def __init__(self, restore=None):
		self.restore = restore

	def __str__(self):
		return 'Torch'
