class Character:
    dead_health = 0

    def __init__(self, race, damage, armor):
        self.race = race
        self.damage = damage
        self.armor = armor
        self.health = 100

        if not isinstance(race, str) or not isinstance(damage, int) or not isinstance(armor, int):
            raise TypeError("Wrong type!")
        elif damage <= 0 or armor < 0:
            raise ValueError("Wrong value!")

    def hit(self, damage, armor):
        self.health = self.health - damage + (damage / armor)

    def restore_health(self, health):
        self.health += health

    @property
    def get_current_health(self):
        return self.health

    def is_dead(self):
        return self.health <= Character.dead_health

    def respawn(self):
        self.health = 100


orc = Character("Orc", 12, 4)

orc.hit(100, orc.armor)
print(orc.get_current_health)
print(orc.is_dead())
orc.hit(40, orc.armor)
print(orc.get_current_health)
print(orc.is_dead())
