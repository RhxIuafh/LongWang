from controller.longwang import Distance
from utils.action import Action
from controller.longwang import Skill
class Fighter:
    
    health = 0
    
    bonus = [1,1,1]

    longmai_set = [0,0,0]
    
    def __init__(self, health, bonus, longmai_set):
        self.health = health
        self.bonus = bonus
        self.longmai_set = longmai_set

    def advance(self):
        print("发动前进!")
        return -1
    
    def back(self):
        print("发动后退!")
        return 1
    
    def stone1(self):
        print("发动突袭!")
        stone1 = Action(Skill.STONE, 2, [Distance.CLOSE], 2, [-1,0,0,1,2,3])
        return stone1
    
    def stone2(self):
        print("发动强袭!")
        stone2 = Action(Skill.STONE, 1, [Distance.MID, Distance.FAR], 1, [-1,0,0,0,1,2])
        return stone2
    
    def scissor1(self):
        print("发动狙击!")
        scissor1 = Action(Skill.SCISSOR, 2, [Distance.MID], 2, [-1,0,0,1,2,3])
        return scissor1
    
    def scissor2(self):
        print("发动爆裂射击!")
        scissor2 = Action(Skill.SCISSOR, 1, [Distance.CLOSE, Distance.FAR], 1, [-1,0,0,0,1,2])
        return scissor2
    
    def cloth1(self):
        print("发动古典咏唱!")
        cloth1 = Action(Skill.CLOTH, 2, [Distance.FAR], 2, [-1,0,0,1,2,3])
        return cloth1
    
    def cloth2(self):
        print("发动新式咏唱!")
        cloth2 = Action(Skill.CLOTH, 1, [Distance.CLOSE, Distance.MID], 1, [-1,0,0,0,1,2])
        return cloth2
        
        
            

    
    