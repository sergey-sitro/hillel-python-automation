class Character:
    dead_health = 0
    _max_hp = 100

    @staticmethod
    def validate_attr_type(attr, attr_name, correct_type):
        if type(attr) is not correct_type:
            raise TypeError(f"{attr_name} must be a {correct_type}, not a {type(attr)}")

    @staticmethod
    def validate_attr_value(attr, attr_name):
        if attr < 0:
            raise ValueError(f"{attr_name} can not be less than 0!")

    def __init__(self, race, damage, armor):
        self.validate_attr_type(race, "Race", str)
        self.race = race

        self.validate_attr_type(damage, "Damage", int)
        self.validate_attr_value(damage, "Damage")
        self.damage = damage

        self.validate_attr_type(armor, "Armor", int)
        self.validate_attr_value(armor, "Armor")
        self.armor = armor

        self._health = Character._max_hp

    def hit(self, damage):
        self.validate_attr_type(damage, "Hit damage", int)
        self.validate_attr_value(damage, "Hit damage")
        self._health = self._health - damage + (damage / self.armor)

        if self._health < Character.dead_health:
            self._health = self.dead_health

    def restore_health(self, health):
        self.validate_attr_type(health, "Restore HP", int)
        self.validate_attr_value(health, "Restore HP")
        self._health += health

        if self._health > Character._max_hp:
            self._health = self._max_hp

    @property
    def current_health(self):
        return self._health

    def is_dead(self):
        return self._health <= self.dead_health

    def respawn(self):
        self._health = self._max_hp


orc = Character("Orc", 1, 5)

orc.hit(1000)
print(orc.current_health)
print(orc.is_dead())
orc.restore_health(1000)
print(orc.current_health)
print(orc.is_dead())
