class Character:
    dead_health = 0

    def __init__(self, race, damage, armor):
        self.race = race
        self.damage = damage
        self.armor = armor
        self.health = 100

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


elf = Character("Elf", 10, 5)
orc = Character("Orc", 12, 4)

orc.hit(100, orc.armor)
print(orc.get_current_health)
print(orc.is_dead())
orc.hit(40, orc.armor)
print(orc.get_current_health)
print(orc.is_dead())
