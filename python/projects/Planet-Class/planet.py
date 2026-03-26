# Jordan Fitzgerald
# 3/26/2026
# Planet

# This module defines a Planet class with attributes for the planet's name, type, and star it orbits. The class includes a method to simulate the planet orbiting its star and a string representation method to display the planet's information. The module also demonstrates the creation of several Planet instances and their functionality.

class Planet:
    def __init__(self, name, planet_type, star):
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')
        if name == '' or planet_type == '' or star == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')
        self.name = name
        self.planet_type = planet_type
        self.star = star
    
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet('Earth', 'Terrestrial', 'Sun')
planet_2 = Planet('Jupiter', 'Gas Giant', 'Sun')
planet_3 = Planet('Kepler-22b', 'Exoplanet', 'Kepler-22')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
