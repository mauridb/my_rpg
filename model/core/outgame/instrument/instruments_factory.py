from model.core.outgame.instrument.dice.dice_object import (
	D4,
	D6,
	D8,
	D10,
	D12,
	D20,
	DRate,
	)
from model.core.outgame.instrument.room.room_object import (
	SingleMissionRoom,
	CampaignRoom,
	WarRoom,
	ClanWarRoom
	)


class D4Factory(object):
	"""
	D4 factory object
	"""
	def get_object(self):
		return D4()


class D6Factory(object):
	"""
	D6 factory object
	"""
	def get_object(self):
		return D6()


class D8Factory(object):
	"""
	D8 factory object
	"""
	def get_object(self):
		return D8()


class D10Factory(object):
	"""
	D10 factory object
	"""
	def get_object(self):
		return D10()


class D12Factory(object):
	"""
	D12 factory object
	"""
	def get_object(self):
		return D12()


class D20Factory(object):
	"""
	D20 factory object
	"""
	def get_object(self):
		return D20()


class DRateFactory(object):
	"""
	DRate factory object
	"""
	def get_object(self):
		return DRate()


class SingleMissionRoomFactory(object):
	"""
	Single mission factory object
	"""

	def get_object(self):
		return SingleMissionRoom()


class CampaignRoomFactory(object):
	"""
	Campaign room factory object
	"""

	def get_object(self):
		return CampaignRoom()


class WarRoomFactory(object):
	"""
	War room factory object
	"""

	def get_object(self):
		return WarRoom()


class ClanWarRoomFactory(object):
	"""
	Clan war factory object
	"""

	def get_object(self):
		return ClanWarRoom()
