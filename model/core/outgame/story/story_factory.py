from model.core.outgame.story.story_object import Story


class StoryFactory(object):
	"""
	Story factory object
	"""

	def get_object(self):
		return Story()
