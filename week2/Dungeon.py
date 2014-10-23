from hero import Hero
from orc import Orc
import math
from entity import Entity
from fight import Fight


class Dungeon():

    def __init__(self, path):
        file = open(path, "r")
        self.map = file.read()
        self.heroes = []
        self._ROW_LENGTH = math.sqrt(len(self.map))
        file.close()

    def print_map(self):
        print (self.map)

    def spawn(self, name, entity):
        self.map = [x for x in self.map]
        for i in range(len(self.map)):
            if self.map[i] == 'S':
                self.heroes.insert(i, [name, entity])
                if isinstance(entity, Hero):
                    self.map[i] = "H"
                else:
                    self.map[i] = "O"
                break
        else:
            self.map = "".join(self.map)
            return False
        self.map = "".join(self.map)
        return True

    def move(self, name, direction):
        self.map = [x for x in self.map]
        if direction == "right":
            step = 1
        elif direction == "left":
            step = - 1
        elif direction == "down":
            step = self._ROW_LENGTH
        elif direction == "up":
            step = - self._ROW_LENGTH

        for i in range(len(self.heroes)):
            if self.heroes[i][0] == name:
                if self.map[i + step] == '.':
                    self.map[i + step] = "H" if isinstance(self.heroes[i][1], Hero) else "O"
                    self.map[i] = '.'
                    self.heroes.insert(i + step, self.heroes[i])
                    self.heroes.pop(i)
                    self.map = "".join(self.map)
                    return True
                elif self.map[i + step] == "H" or self.map[i + step] == "O":
                    self.fight = Fight(self.heroes[i][1], self.heroes[i + step][1])
                    self.fight.simulate_fight()
                    if self.heroes[i][1].is_alive():
                        self.map[i + step] = "H" if isinstance(self.heroes[i][1], Hero) else "O"
                        self.map[i] = '.'
                        self.heroes.insert(i + step, self.heroes[i])
                        self.heroes.pop(i)
                    else:
                        self.map[i] = '.'
                        self.heroes.pop(i)
                    self.map = "".join(self.map)

                    return True

                elif self.map[i + step] == '\n':
                    if self.map[i + step + 1] == '.':
                        self.map[i + step + 1] = "H" if isinstance(self.heroes[i][1], Hero) else "O"
                        self.map[i] = '.'
                        self.heroes.insert(i + step + 1, self.heroes[i])
                        self.heroes.pop(i)
                        self.map = "".join(self.map)
                        return True
                    elif self.map[i + step + 1] == "H" or self.map[i + step + 1] == "O":
                        self.fight = Fight(self.heroes[i][1], self.heroes[i + step + 1][1])
                        self.fight.simulate_fight()
                        if self.heroes[i][1].is_alive():
                            self.map[i + step + 1] = "H" if isinstance(self.heroes[i][1], Hero) else "O"
                            self.map[i] = '.'
                            self.heroes.insert(i + step + 1, self.heroes[i])
                            self.heroes.pop(i)
                        else:
                            self.map[i] = '.'
                            self.heroes.pop(i)
                        self.map = "".join(self.map)
                        return True
        self.map = "".join(self.map)
        return False






