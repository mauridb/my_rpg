import random

from model.core.game_factory import (
	IngameFactory,
	OutgameFactory
	)
from model.core.outgame.instrument.instruments_factory import (
	D4Factory,
	D6Factory,
	D8Factory,
	D10Factory,
	D12Factory,
	D20Factory,
	DRateFactory,
	SingleMissionRoomFactory,
	CampaignRoomFactory,
	WarRoomFactory,
	ClanWarRoomFactory,
	)

class DeDSystem(object):

	def __init__(self, factory=None):
		self.factory = factory

	def show_object_factory(self):
		obj = self.factory().get_object()
		obj_id = obj.get_object_id()
		print("OBJECT: ", obj)
		print("OBJECT ID: ", obj_id)


# Get factory method
def get_factory():

	return random.choice([
		IngameFactory,
		OutgameFactory,
		SingleMissionRoomFactory,
		CampaignRoomFactory,
		WarRoomFactory,
		ClanWarRoomFactory,
		D4Factory,
		D6Factory,
		D8Factory,
		D10Factory,
		D12Factory,
		D20Factory,
		DRateFactory
		])