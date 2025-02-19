#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", 
    "French Bulldog", "Pug","Breed", "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        # Validate name first
        self.name = name  # This triggers the name setter
        # If name is invalid, no need to check breed.
        if hasattr(self, '_name') == False:  # Check if name is valid (setter was triggered)
            return
        # Now check breed
        self.breed = breed  # This triggers the breed setter

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed == "":
            self._breed = "Mutt"
        else:
            self._breed = breed

    breed = property(get_breed, set_breed)
