import humanize

class BaseSpaceClass:
    pass


class ValidatorMixin:
    @staticmethod
    def _validate_entity_attr_type(attr, attr_name, cottect_type):
        if type(attr) is not cottect_type:
            raise TypeError(f"{attr_name} must be a {cottect_type}, not a {type(attr)}")

    @staticmethod
    def _validate_entity_attr_gt_0(attr, attr_name):
        if attr <= 0:
            raise ValueError(f"{attr_name} must be greater than 0")


class AstronomicalEntity(BaseSpaceClass, ValidatorMixin):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"AstronomicalEntity: '{self.name}'"

    def __repr__(self):
        return f"AstronomicalEntity(name='{self.name}')"
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise AttributeError(f"the name of the object cannot be changed")
        self._validate_entity_attr_type(name, "name", str)
        self.__name = name



class AstronomicalObject(AstronomicalEntity):
    def __init__(self, name, radius, mass):
        super(AstronomicalObject, self).__init__(name)
        self.radius = radius
        self.mass = mass

    def __str__(self):
        return f"{self.name} with a radius of {self.human_readable_radius} and a mass of {self.human_readable_mass}"

    def __repr__(self):
        return f"AstronomicalObject(name='{self.name}', radius={self.radius}, mass={self.mass})"

    @property
    def human_readable_radius(self):
        return f"{humanize.intword(self.radius)} km"

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if hasattr(self, "radius"):
            raise AttributeError(f"the radius of the object cannot be changed")
        self._validate_entity_attr_type(radius, "radius", int)
        self._validate_entity_attr_gt_0(radius, "radius")
        self.__radius = radius

    @property
    def human_readable_mass(self):
        return f"{humanize.intword(self.mass)} tons"

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        if hasattr(self, "mass"):
            raise AttributeError(f"the mass of the object cannot be changed")
        self._validate_entity_attr_type(mass, "mass", int)
        self._validate_entity_attr_gt_0(mass, "mass")
        self.__mass = mass



class Star(AstronomicalObject):
    def __init__(self, name, radius, mass, temperature):
        super(Star, self).__init__(name, radius, mass)
        self.temperature = temperature

    def __str__(self):
        return f"{self.name} star with a radius of {self.human_readable_radius}, a mass of {self.human_readable_mass} and temperature of {self.human_readable_temperature}"

    def __repr__(self):
        return f"Star(name='{self.name}', radius={self.radius}, mass={self.mass}, temperature={self.temperature})"

    @property
    def human_readable_temperature(self):
        return f"{humanize.intword(self.temperature)} degrees Kelvin"

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature):
        if hasattr(self, "temperature"):
            raise AttributeError(f"the temperature of the star cannot be changed")
        self._validate_entity_attr_type(temperature, "temperature", int)
        self._validate_entity_attr_gt_0(temperature, "temperature")
        self.__temperature = temperature


class Planet(AstronomicalObject):
    def __init__(self, name, radius, mass, distance_to_star_from, distance_to_star_to):
        super(Planet, self).__init__(name, radius, mass)
        self.distance_to_star_from = distance_to_star_from
        self.distance_to_star_to = distance_to_star_to

    def __str__(self):
        return f"{self.name} planet with a radius of {self.human_readable_radius}, a mass of {self.human_readable_mass} and distance to star in average {self.human_readable_avarege_distance_to_star}"

    def __repr__(self):
        return f"Planet(name='{self.name}', radius={self.radius}, mass={self.mass}, distance_to_star_from={self.distance_to_star_from}, distance_to_star_to={self.distance_to_star_to})"

    @property
    def human_readable_distance_to_star_from(self):
        return f"{humanize.intword(self.distance_to_star_from)} km"

    @property
    def distance_to_star_from(self):
        return self.__distance_to_star_from

    @distance_to_star_from.setter
    def distance_to_star_from(self, distance_to_star_from):
        if hasattr(self, "distance_to_star_from"):
            raise AttributeError(f"the distance_to_star_from of the planet cannot be changed")
        self._validate_entity_attr_type(distance_to_star_from, "distance_to_star_from", int)
        self._validate_entity_attr_gt_0(distance_to_star_from, "distance_to_star_from")
        self.__distance_to_star_from = distance_to_star_from

    @property
    def human_readable_distance_to_star_to(self):
        return f"{humanize.intword(self.distance_to_star_to)} km"

    @property
    def distance_to_star_to(self):
        return self.__distance_to_star_to

    @distance_to_star_to.setter
    def distance_to_star_to(self, distance_to_star_to):
        if hasattr(self, "distance_to_star_to"):
            raise AttributeError(f"the distance_to_star_to of the planet cannot be changed")
        self._validate_entity_attr_type(distance_to_star_to, "distance_to_star_to", int)
        self._validate_entity_attr_gt_0(distance_to_star_to, "distance_to_star_to")
        self.__distance_to_star_to = distance_to_star_to

    @property
    def avarege_distance_to_star(self):
        return (self.distance_to_star_from + self.distance_to_star_to) // 2

    @property
    def human_readable_avarege_distance_to_star(self):
        return f"{humanize.intword(self.avarege_distance_to_star)} km"


class StarSystem(AstronomicalEntity):
    def __init__(self, name, star, *planets):
        super(StarSystem, self).__init__(name)
        self.star = star
        self.planets = planets

    def __str__(self):
        return f"{self.name} with the star {self.star.name} and the planets {', '.join([planet.name for planet in self.planets])}"

    def __repr__(self):
        return f"StarSystem('{self.name}', {self.star.__repr__()}, *({', '.join([planet.__repr__() for planet in self.planets])}))"

    def __add__(self, other):
        self._validate_entity_attr_type(other, "planet", Planet)
        if other in self.planets:
            raise ValueError(f"planet {other.name} already in {self.name}")
        return StarSystem(
            self.name,
            self.star,
            *sorted(
                self.planets + (other, ),
                key=lambda planet: planet.avarege_distance_to_star
            )
        )

    @property
    def star(self):
        return self.__star

    @star.setter
    def star(self, star):
        if hasattr(self, "star"):
            raise AttributeError(f"the star of the star system cannot be changed")
        self._validate_entity_attr_type(star, "star", Star)
        self.__star = star

    @property
    def human_readable_star(self):
        return str(self.star)

    @property
    def planets(self):
        return self.__planets

    @planets.setter
    def planets(self, planets):
        if hasattr(self, "planets"):
            raise AttributeError(f"the planets of the star system cannot be changed")
        self._validate_entity_attr_gt_0(len(planets), "number of planets")
        if len(planets) != len(set(planets)):
            raise ValueError(f"planets should be unique")
        self._validate_planets_order(planets)
        for planet in planets:
            self._validate_entity_attr_type(planet, "planet", Planet)
        self.__planets = planets

    @property
    def human_readable_planets(self):
        return "\n".join((f"{position}. {str(planet)}" for position, planet in enumerate(self.planets, 1)))

    @staticmethod
    def _validate_planets_order(planets):
        planets_distances = [planet.avarege_distance_to_star for planet in planets]
        if planets_distances != sorted(planets_distances):
            raise ValueError(f"planets must be provided in the correct order")

    def get_info(self):
        star = self.human_readable_star
        planets = self.human_readable_planets
        return f"{star}\n{planets}"


sun = Star("Sun", 695700, 19884*10**26, 157*10**5)

mercury = Planet("Mercury", 2440, 33011*10**19, 46*10**6, 7*10**7)
venus = Planet("Venus", 6052, 48675*10**20, 108*10**6-72360, 108*10**6+72360)
earth = Planet("Earth", 6371, 597237*10**19, 147*10**6, 152*10**6)
mars = Planet("Mars", 3390, 64171*10**19, 206*10**6, 249*10**6)

solar_system = StarSystem("Solar System", sun, mercury, earth, mars)
