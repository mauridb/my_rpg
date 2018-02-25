import uuid


class Room(object):
	"""
	Room object
	"""

	def __init__(self, room_type=None, effort_time=None):
		self.room_type = room_type
		self.effort_time = effort_time

	def __str__(self):
		return self.room_type


class SingleMissionRoom(Room):
	"""
	Single mission room
	"""
	def __init__(self, room_type='Single Mission', effort_time='30min'):
		super().__init__(room_type, effort_time)

	def __str__(self):
		return super().__str__()

	def get_object_id(self):
		return str(uuid.uuid1())


class CampaignRoom(Room):
	"""
	Campaign room
	"""
	def __init__(self, room_type='Campaign', effort_time='20min'):
		super().__init__(room_type, effort_time)

	def __str__(self):
		return super().__str__()

	def get_object_id(self):
		return str(uuid.uuid1())


class WarRoom(Room):
	"""
	War room
	"""
	def __init__(self, room_type='War', effort_time='20min'):
		super().__init__(room_type, effort_time)

	def __str__(self):
		return super().__str__()

	def get_object_id(self):
		return str(uuid.uuid1())


class ClanWarRoom(Room):
	"""
	Clan War room
	"""
	def __init__(self, room_type='Clan War', effort_time='120min'):
		super().__init__(room_type, effort_time)

	def __str__(self):
		return super().__str__()

	def get_object_id(self):
		return str(uuid.uuid1())
