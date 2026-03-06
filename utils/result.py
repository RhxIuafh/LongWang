from controller.longwang import Skill
class Result:
    # 命中 1表示1号，2表示2号
    hit = 1
    # 伤害
    damage = 0
    # 属性
    attribute = Skill.STONE
    # 龙脉改变
    longmai_change = 0

    def __init__(self, hit, damage, attribute, longmai_change):
        self.hit = hit
        self.damage = damage
        self.attribute = attribute
        self.longmai_change = longmai_change
    
    