import random
import uuid


class Equipement(object):
	"""
	Equipement object
	"""
	def __init__(self, category=None):
		self.category = category

	def __str__(self):
		return str(self.category)

	def _set_stats(self):
		return {
		'atk': random.randint(0, 10),
		'def': random.randint(0, 10),
		'weight': random.randint(0, 10)
		}

	def get_object_id(self):
		return str(uuid.uuid1())
