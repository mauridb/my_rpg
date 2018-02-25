import random
from model.core.outgame.rule.equipement.equipement_object import Equipement
from model.core.outgame.rule.equipement.weapon.weapon_object import (
	Sword,
	Knife,
	Staff,
	Hammer,
	Arch
	)
from model.core.outgame.rule.equipement.armor.armor_object import (
	Armor,
	Helm,
	Shield,
	Shoes
	)
from model.core.outgame.rule.equipement.accessory.accessory_object import (
	Potion,
	Rope,
	Stone,
	Torch
	)


def get_equip():
	return random.choice([
		Sword(),
		Knife(),
		Staff(),
		Hammer(),
		Arch(),
		Armor(),
		Helm(),
		Shield(),
		Shoes(),
		Potion(),
		Stone(),
		Torch(),
		Rope()
		])


class EquipementFactory(object):
	"""
	Equipement object factory
	"""
	def get_object(self):
		return Equipement(category=get_equip())