import random

class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

class AnimalGame:
    def __init__(self, animals):
        self.animals = animals

    def run_game(self):
        print("Welcome to the Animal Game!")
        score = 0
        for i in range(5):
            animal = random.choice(self.animals)
            print
