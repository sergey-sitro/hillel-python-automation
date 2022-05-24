class Character:
    dead_health = 0

    def __init__(self, race, damage, armor):
        try:
            self.race = race

            if not isinstance(race, str):
                raise TypeError

        except TypeError:
            print("Race can be 'str' only!")
            raise TypeError

        try:
            self.damage = damage

            if not isinstance(damage, int):
                raise TypeError
            elif damage <= 0:
                raise ValueError

        except TypeError:
            print("Damage can be int only")
            raise TypeError

        except ValueError:
            print("Damage attribute should be > 0!")
            raise ValueError

        try:
            self.armor = armor

            if not isinstance(armor, int):
                raise TypeError
            elif armor < 0:
                raise ValueError

        except TypeError:
            print("Armor can be int only!")
            raise TypeError

        except ValueError:
            print("Armor attribute should be not less than 0!")
            raise ValueError

        self.health = 100

    def hit(self, damage):
        try:
            self.health = self.health - damage + (damage / self.armor)

            if not isinstance(damage, int):
                raise TypeError
            elif damage < 0:
                raise ValueError

        except TypeError:
            print("Can not hit by a string!")
            raise TypeError

        except ValueError:
            print("Can not hit less than 0 hit points!")
            raise ValueError

    def restore_health(self, health):
        try:
            self.health += health

            if not isinstance(health, int):
                raise TypeError
            elif health <= 0:
                raise ValueError

        except TypeError:
            print("You can not heal by a string!")
            raise ValueError

        except ValueError:
            print("You can't hurt yourself by healing!")
            raise ValueError

    @property
    def current_health(self):
        return self.health

    def is_dead(self):
        return self.health <= self.dead_health

    def respawn(self):
        self.health = 100


orc = Character("Orc", 10, 5)

orc.hit(100)
print(orc.current_health)
print(orc.is_dead())
orc.hit(10)
orc.restore_health(-1)
print(orc.current_health)
print(orc.is_dead())
