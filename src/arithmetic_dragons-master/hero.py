# coding: utf-8
# license: GPLv3
from gameunit import *
from random import random
from abc import abstractmethod

class Hero (Attacker):
    def __init__(self, name):
        self._name = name
        self._experience=0
    def Give_Up(self):
        self.health=0
    @abstractmethod
    def Run_Away(self, enemy):
        pass


class Fighter(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self._attack = 50
        self._class = 'Fighter'
    def armour(self):
        armour=1-(self._experience/100)
        return armour
    def Run_Away(self, enemy):
        self.health-=2*enemy._attack()*self.armour()
class Wizard (Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health = 60
        self._attack = 100
        self._class = 'Wizard'
    def Run_Away(self, enemy):
        print ('маг создает магический туман и убегает безнаказанным')
class Rogue (Hero):
     def __init__ (self, name):
         super().__init__(name)
         self.health = 80
         self._attack = 40
         self._class = 'Rogue'
     def armour(self):
        armour = random()-self._experience/100
        return armour
     def Run_Away(self, enemy):
         dodge=self.armour()
         self.health-= 0.5*enemy._attack*dodge
         self._experience+= 5*dodge
