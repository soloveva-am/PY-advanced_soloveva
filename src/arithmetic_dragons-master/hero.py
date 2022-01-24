# coding: utf-8
# license: GPLv3
from gameunit import *
from random import random

class Hero (Attacker):
    def __init__(self, name):
        self._name = name
        self._experience=0
    def Give_Up:
        self._health=0


class Fighter(Hero):
    def __init__(self, name):
        super.__init__(name)
        self._health = 100
        self._attack = 50
        self._class = 'Fighter'
    def armour(self):
        armour=1-(self._experience/100)
        return armour
 class Wizard (Hero):
    def __init__(self):
        super.__init__(name):
        self._health = 60
        self._attack = 100
        self._class = 'Wizard'
class Rogue (Hero)
     def __init__ (self):
         super.__init__(name):
         self._health = 80
         self._attack = 40
         self._class = 'Rogue'
    def armour(self):
        armour = random()
        return random()