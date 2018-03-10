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
from model.core.outgame.rule.character.character_factory import CharacterFactory
from model.core.outgame.rule.enemy.enemy_factory import EnemyFactory
from model.core.outgame.rule.enemy.boss.boss_factory import BossFactory
from model.core.outgame.rule.equipement.equipement_factory import EquipementFactory
from model.core.outgame.rule.equipement.spell.spell_factory import SpellFactory
from model.core.outgame.user.user_factory import UserFactory
from model.core.outgame.user.auth.authentication_factory import AuthenticationFactory
from model.core.outgame.user.registration.registration_factory import RegistrationFactory
from model.core.outgame.user.login.login_factory import LoginFactory
from model.core.outgame.story.story_factory import StoryFactory
from model.core.outgame.story.dungeon.dungeon_factory import DungeonFactory 
from model.core.outgame.story.mission.mission_factory import MissionFactory


class DeDSystem(object):

	def __init__(self, factory=None):
		self.factory = factory

	def show_object_factory(self):
		obj = self.factory().get_object()
		# print(obj)
		obj_id = obj.get_object_id()
		print("OBJECT: ", obj)
		print("OBJECT ID: ", obj_id)


# Get factory method
def get_factory():

	return random.choice([
		# IngameFactory,
		# OutgameFactory,
		# SingleMissionRoomFactory,
		# CampaignRoomFactory,
		# WarRoomFactory,
		# ClanWarRoomFactory,
		# D4Factory,
		# D6Factory,
		# D8Factory,
		# D10Factory,
		# D12Factory,
		# D20Factory,
		# DRateFactory,
		# CharacterFactory,
		# EnemyFactory,
		# BossFactory,
		# EquipementFactory,
		# SpellFactory,
		# UserFactory,
		# AuthenticationFactory,
		# RegistrationFactory,
		# LoginFactory,
		# StoryFactory,
		# DungeonFactory,
		MissionFactory
		])