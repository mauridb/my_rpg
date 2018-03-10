import random

from model.core.outgame.story.dungeon.dungeon_object import (
	Dungeon,
	NormalDungeon,
	HardDungeon,
	ExpertDungeon,
	MasterDungeon,
	TormentOneDungeon,
	TormentTwoDungeon,
	TormentThreeDungeon
	)


def get_dungeon_object():
	return random.choice([
		NormalDungeon(),
		HardDungeon(),
		ExpertDungeon(),
		MasterDungeon(),
		TormentOneDungeon(),
		TormentTwoDungeon(),
		TormentThreeDungeon()
		])

class DungeonFactory(object):
	"""
	Dungeon factory object
	"""
	def get_object(self):
		return Dungeon(d_level=get_dungeon_object())
