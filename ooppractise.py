from networkx import hits


class pokemon:
    def __init__(self, health, attack, mana):
        self.health = health
        self.attack = attack
        self.mana = mana

    def hit(self, attack):
        self.health = self.health - attack
        return self.health

    def magicattack(self, attack):
        self.health = self.health - (attack * self.mana)
        return self.health

    def gethealth(self):
        return self.health

class pikachu(pokemon):
    def __init__(self, health, attack, mana):
        super().__init__(health, attack, mana)
pikachu1 = pikachu(100,20,30)
pikachu2 = pikachu(150,15,15)
hit(pikachu1, pikachu2.attack)