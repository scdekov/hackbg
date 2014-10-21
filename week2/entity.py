from weapon import Weapon


class Entity():

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.weapon = None


    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, dmg):
        if dmg > self.health:
            self.health = 0
        else:
            self.health -= dmg

    def take_healing(self, heal):
        if self.health == 0:
            return False
        elif self.health + heal > self._MAX_HEALTH:
            self.health = self._MAX_HEALTH
        else:
            self.health += heal
        return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        return self.weapon is not None

    def attack(self):
        if self.has_weapon():
            if self.weapon.critical_hit():
                return self.weapon.damage * 2
            else:
                return self.weapon.damage
        else:
            return 0

