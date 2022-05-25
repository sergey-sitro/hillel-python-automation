class Character:
    dead_health = 0

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

        self.health = 100

    def hit(self, damage):
        self.validate_attr_type(damage, "Hit damage", int)
        self.validate_attr_value(damage, "Hit damage")
        self.health = self.health - damage + (damage / self.armor)

    def restore_health(self, health):
        self.validate_attr_type(health, "Restore HP", int)
        self.validate_attr_value(health, "Restore HP")
        self.health += health

    @property
    def current_health(self):
        return self.health

    def is_dead(self):
        return self.health <= self.dead_health

    def respawn(self):
        self.health = 100


orc = Character("Orc", 1, 5)

orc.hit(100)
print(orc.current_health)
print(orc.is_dead())
orc.hit(1)
orc.restore_health("Str")
print(orc.current_health)
print(orc.is_dead())
