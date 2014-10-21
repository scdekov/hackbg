from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        if berserk_factor > 2.0:
            self.berserk_factor = 2.0
        elif berserk_factor < 1.0:
            self.berserk_factor = 1.0
        else:
            self.berserk_factor = berserk_factor

    def attack(self):
        if self.has_weapon():
            if self.weapon.critical_hit():
                return self.weapon.damage * self.berserk_factor * 2
            else:
                return self.weapon.damage * self.berserk_factor
        else:
            return 0

