class Character:
    dead_health = 0
    max_hp = 100

    @staticmethod
    def validate_attr_type(attr, attr_name, correct_type):
        if type(attr) is not correct_type:
            raise TypeError(f"{attr_name} must be a {correct_type}, not a {type(attr)}")

    @staticmethod
    def validate_attr_value(attr, attr_name):
        if attr < 0:
            raise ValueError(f"{attr_name} can not be less than 0!")

    @staticmethod
    def validate_hp(health):
        if health < Character.dead_health or health > Character.max_hp:
            raise ValueError(f"Health should be between {Character.dead_health} and {Character.max_hp}")

    def __init__(self, race, damage, armor):
        self.validate_attr_type(race, "Race", str)
        self.race = race

        self.validate_attr_type(damage, "Damage", int)
        self.validate_attr_value(damage, "Damage")
        self.damage = damage

        self.validate_attr_type(armor, "Armor", int)
        self.validate_attr_value(armor, "Armor")
        self.armor = armor

        self._health = 100

    def hit(self, damage):
        self.validate_attr_type(damage, "Hit damage", int)
        self.validate_attr_value(damage, "Hit damage")
        self._health = self._health - damage + (damage / self.armor)
        self.validate_hp(self._health)

    def restore_health(self, health):
        self.validate_attr_type(health, "Restore HP", int)
        self.validate_attr_value(health, "Restore HP")
        self._health += health
        self.validate_hp(self._health)

    @property
    def current_health(self):
        return self._health

    def is_dead(self):
        return self._health <= self.dead_health

    def respawn(self):
        self._health = 100


orc = Character("Orc", 1, 5)

orc.hit(10)
print(orc.current_health)
print(orc.is_dead())
orc.restore_health(125)
print(orc.current_health)
print(orc.is_dead())
