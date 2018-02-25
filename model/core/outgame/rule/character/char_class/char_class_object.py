class CharacterClass(object):
	"""
	Class of character object to extend
	"""
	def __init__(self, char_class=None, description=None):
		self.char_class = char_class
		self.description = description


class Wizard(CharacterClass):
	"""
	Wizard character class object
	"""
	def __init__(self):
		super().__init__(char_class='Wizard')


class Warrior(CharacterClass):
	"""
	Warrior character class object
	"""
	def __init__(self):
		super().__init__(char_class='Warrior')


class Ninja(CharacterClass):
	"""
	Ninja character class object
	"""
	def __init__(self):
		super().__init__(char_class='Ninja')


class Druid(CharacterClass):
	"""
	Druid character class object
	"""
	def __init__(self):
		super().__init__(char_class='Druid')


class Monk(CharacterClass):
	"""
	Monk character class object
	"""
	def __init__(self):
		super().__init__(char_class='Monk')


class Priest(CharacterClass):
	"""
	Priest character class object
	"""
	def __init__(self):
		super().__init__(char_class='Priest')
