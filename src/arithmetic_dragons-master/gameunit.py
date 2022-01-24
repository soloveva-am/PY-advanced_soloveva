# coding: utf-8
# license: GPLv3
from abc import ABC

class Attacker(ABC):
    health = None
    _attack = None

    def attack(self, target):
        target.health -= self._attack*target.armour()

    def is_alive(self):
        return self.health > 0
    def armour(self):
        return 1
    