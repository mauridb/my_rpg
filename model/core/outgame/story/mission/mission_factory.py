import random

from model.core.outgame.story.mission.mission_object import (
	Mission,
	E,
	D,
	C,
	B,
	A,
	S,
	SS,
	Legend
	)


def get_mission_object():
	return random.choice([
		E(),
		D(),
		C(),
		B(),
		A(),
		S(),
		SS(),
		Legend()
		])


class MissionFactory(object):
	"""
	Mission factory object
	"""

	def get_object(self):
		return Mission(grade=get_mission_object())
