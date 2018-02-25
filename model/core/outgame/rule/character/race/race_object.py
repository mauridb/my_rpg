class CharacterRace(object):
	"""
	Race object to extend
	"""
	def __init__(self, race=None, description=None):
		self.race = race
		self.description = description


class Human(CharacterRace):
	"""
	Human specific raze object
	"""
	def __init__(self):
		super().__init__(race='Human')


class Elf(CharacterRace):
	"""
	Elf specific raze object
	"""
	def __init__(self):
		super().__init__(race='Elf')


class Dwarf(CharacterRace):
	"""
	Dwarf specific raze object
	"""
	def __init__(self):
		super().__init__(race='Dwarf')


class Gnome(CharacterRace):
	"""
	Gnome specific raze object
	"""
	def __init__(self):
		super().__init__(race='Gnome')


class Orc(CharacterRace):
	"""
	Orc specific raze object
	"""
	def __init__(self):
		super().__init__(race='Orc')
