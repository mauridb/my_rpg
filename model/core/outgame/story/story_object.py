import uuid
import random


class Story(object):
	"""
	Story object
	"""

	def __init__(self, title=None):
		self.title = title

	def _start(self):
		return 'start'

	def _middle(self):
		return 'middle'

	def _end(self):
		return 'end'

	def get_object_id(self):
		return str(uuid.uuid1())

	def __str__(self):
		return 'Story'
