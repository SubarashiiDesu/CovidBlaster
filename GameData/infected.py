# TODO: COMPLETE INFECTED IMPLEMENTATION
from character import Character


# Infected inherits from character class
class Infected(Character):
    def __init__(self, dimensions, location):
        super().__init__(dimensions, location)