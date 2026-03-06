class Action:

    attribute = 0

    damage = 0
    
    range = []

    longmai_change = 0

    bonus = []

    def __init__(self, attribute, damage, range, longmai_change, bonus):
        self.attribute = attribute
        self.damage = damage
        self.range = range
        self.longmai_change = longmai_change
        self.bonus = bonus

    