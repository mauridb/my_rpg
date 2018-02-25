from model.core.outgame.rule.equipement.equipement_object import Equipement


class Sword(Equipement):
	"""
	Sword object
	"""
	def __init__(self):
		self.stats = super()._set_stats()

	def __str__(self):
		return 'Sword'


class Knife(Equipement):
	"""
	Knife object
	"""
	def __init__(self):
		self.stats = super()._set_stats()

	def __str__(self):
		return 'Knife'


class Hammer(Equipement):
	"""
	Hammer object
	"""
	def __init__(self):
		self.stats = super()._set_stats()

	def __str__(self):
		return 'Hammer'


class Arch(Equipement):
	"""
	Arch object
	"""
	def __init__(self):
		self.stats = super()._set_stats()

	def __str__(self):
		return 'Arch'


class Staff(Equipement):
	"""
	Staff object
	"""
	def __init__(self):
		self.stats = super()._set_stats()

	def __str__(self):
		return 'Staff'
