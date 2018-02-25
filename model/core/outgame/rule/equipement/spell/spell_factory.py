import random

from model.core.outgame.rule.equipement.spell.spell_object import (
	Spell,
	Fire,
	Water,
	Earth,
	Wind
	)

def get_spell():
	return random.choice([
		Fire(),
		Water(),
		Earth(),
		Wind(),
		])


class SpellFactory(object):
	"""
	Spell factory object
	"""
	def get_object(self):
		return Spell(spell_type=get_spell()) 
