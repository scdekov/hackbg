import random


class Weapon():

    def __init__(self, type, damage, critical_strike_percent):
            self._set_critical_strike_percent(critical_strike_percent)
            self.type = type
            self.damage = damage

    def _set_critical_strike_percent(self, critical_strike_percent):
        if critical_strike_percent > 1.0 or critical_strike_percent < 0.0:
            raise ValueError
        else:
            self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        return random.random() <= self.critical_strike_percent
