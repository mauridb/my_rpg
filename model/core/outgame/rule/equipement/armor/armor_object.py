from model.core.outgame.rule.equipement.equipement_object import Equipement


class Armor(Equipement):
	"""
	Armor object
	"""
	def __init__(self):
		self.stats = super()._set_stats()

	def __str__(self):
		return 'Armor'


class Helm(Equipement):
	"""
	Helm object
	"""
	def __init__(self):
		self.stats = super()._set_stats()

	def __str__(self):
		return 'Helm'


class Shoes(Equipement):
	"""
	Shoes object
	"""
	def __init__(self):
		self.stats = super()._set_stats()

	def __str__(self):
		return 'Shoes'


class Shield(Equipement):
	"""
	Shield object
	"""
	def __init__(self):
		self.stats = super()._set_stats()

	def __str__(self):
		return 'Shield'
