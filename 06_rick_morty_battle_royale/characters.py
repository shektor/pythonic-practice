import random


class Player:

    MAX_MODIFIER = 12
    MIN_ATTACK = 1
    MIN_DEFENSE = 6

    def __init__(self, name, level = 1):
        self.name = name
        self.level = level


    def __repr__(self):
        return '{}[{}]'.format(self.name, self.level)


    def attack(self):
        attack = self.attack_modifier() * self.level

        return attack


    def defense(self):
        defense = self.defense_modifier() * self.level

        return defense


    def attack_modifier(self):
        modifier = random.randint(self.MIN_ATTACK, self.MAX_MODIFIER)

        return modifier


    def defense_modifier(self):
        modifier = random.randint(self.MIN_DEFENSE, self.MAX_MODIFIER)

        return modifier


class Alien(Player):

    def __init__(self, name, level, super_power = 2):
        super().__init__(name, level)
        self.super_power = super_power


    def attack_modifier(self):
        modifier = super().attack_modifier()
        super_modifier = modifier * self.super_power

        return super_modifier
