
from enum import Enum

# 斗气
class Dice(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

# 距离
class Distance(Enum):
    CLOSE = 0
    MID = 1
    FAR = 2

# 技能属性
class Skill(Enum):
    STONE = 0
    SCISSOR = 1
    CLOTH = 2
    MOVE = 3

# 动作
class Actions(Enum):
    ADVANCE = 0
    BACK = 1
    STONEA = 2
    STONEB = 3
    SCISSORSA = 4
    SCISSORSB = 5
    CLOTHA = 6
    CLOTHB = 7


class LongMai:
    longmai = [3, 3, 3]

    distance = Distance.MID
    
    def __init__(self, longmai, distance):
        self.longmai = longmai
        self.distance = distance
        
    
    def get_red(self):
        return self.longmai[Dice.RED.value]
    
        
    def set_red(self, red):
        if red > 6:
            red = 6
        elif red <= 0:
            red = 1
        self.longmai[Dice.RED.value] = red

    def get_green(self):
        return self.longmai[Dice.GREEN.value]
    
        
    def set_green(self, green):
        if green > 6:
            green = 6
        elif green <= 0:
            green = 1
        self.longmai[Dice.GREEN.value] = green

    def get_blue(self):
        return self.longmai[Dice.BLUE.value]
    
        
    def set_blue(self, blue):
        if blue > 6:
            blue = 6
        elif blue <= 0:
            blue = 1
        self.longmai[Dice.BLUE.value] = blue

    def get_longmai(self):
        return self.longmai
    
    def set_longmai(self, longmai):
        for i in range(3):
            if longmai[i] > 6:
                longmai[i] = 6
            elif longmai[i] < 1:
                longmai[i] = 1
        self.longmai = longmai

    def set_distance(self, distance):
        self.distance = distance
    
    def get_distance(self):
        return self.distance







