# https://www.reddit.com/r/programminghorror/comments/1e0qque/i_like_oneliners/

# Setup
def print_bonus(bonus):
	return bonus


class Value:
	bonus_a = 1
	bonus_b = 2
	bonus_c = 3


# Before
class Thing1:
	def __init__(self, damage_modifiers_applied: dict):
		self.damage_modifiers_applied = damage_modifiers_applied
	
	def _debug_bonuses(self, value: object, name: str, modifier: str):
		string = f"- *{name}*:\n{'\n'.join([f" > {x.capitalize()}: {print_bonus(value.__dict__[x])}" for x in self.damage_modifiers_applied[modifier]])}\n"
		return string
	

# Before: tests
thing = Thing1({
	"mod_a": ["bonus_a"],
	"mod_b": ["bonus_b", "bonus_c"],
})

actual = thing._debug_bonuses(Value, "alice", "mod_a")
assert actual == "- *alice*:\n > Bonus_a: 1\n"

actual = thing._debug_bonuses(Value, "bob", "mod_b")
assert actual == "- *bob*:\n > Bonus_b: 2\n > Bonus_c: 3\n"


# After
class Thing2:
	def __init__(self, damage_modifiers_applied: dict):
		self.damage_modifiers_applied = damage_modifiers_applied
	
	def _debug_bonuses(self, value: object, name: str, damage_mod: str):
		bonus_strings = []

		for bonus in self.damage_modifiers_applied[damage_mod]:
			bonus_name = bonus.capitalize()
			bonus_value = value.__dict__.get(bonus)
			bonus_strings.append(f" > {bonus_name}: {bonus_value}")

		return f"- *{name}*:\n{"\n".join(bonus_strings)}\n"


# After: tests
thing = Thing2({
	"mod_a": ["bonus_a"],
	"mod_b": ["bonus_b", "bonus_c"],
})

actual = thing._debug_bonuses(Value, "alice", "mod_a")
assert actual == "- *alice*:\n > Bonus_a: 1\n"

actual = thing._debug_bonuses(Value, "bob", "mod_b")
assert actual == "- *bob*:\n > Bonus_b: 2\n > Bonus_c: 3\n"

