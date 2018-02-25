import random
from model.core.outgame.rule.character.character_object import Character
from model.core.outgame.rule.character.race.race_object import (
	Human,
	Elf,
	Dwarf,
	Gnome,
	Orc
	)
from model.core.outgame.rule.character.char_class.char_class_object import (
	Wizard,
	Warrior,
	Ninja,
	Druid,
	Monk,
	Priest
	)


def get_race():
	return random.choice([
		Human(),
		Elf(),
		Dwarf(),
		Orc(),
		Gnome()
		])


def get_class():
	return random.choice([
		Wizard(),
		Warrior(),
		Druid(),
		Ninja(),
		Monk(),
		Priest()
		])


class CharacterFactory(object):
	"""
	Character factory
	"""

	def get_object(self):
		return Character(race=get_race(), char_class=get_class())
