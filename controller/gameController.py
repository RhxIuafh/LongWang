from utils.action import Action
from controller.longwang import Skill, Distance
from utils.result import Result


class GameController:

    def __init__(self, longmai):
        self.longmai = longmai

    def get_longmai(self):
        return self.longmai

    # 距离结算
    def distance_settle(self, card1, card2):
        distance_amend = 0
        if not isinstance(card1, Action):
            distance_amend += card1
        
        if not isinstance(card2, Action):
            distance_amend += card2
        
        new_distance = self.longmai.get_distance().value + distance_amend

        if new_distance < 0:
            new_distance = 0
        elif new_distance > 2:
            new_distance = 2
        
        self.longmai.set_distance(Distance(new_distance))

    # 伤害结算
    def damage_settle(self, card1, card2, fighter1,fighter2):
        damage = 0
        hit1 = 0
        hit2 = 0
        if isinstance(card1, Action) and isinstance(card2, Action):
            # 范围结算
            if self.longmai.get_distance() in card1.range:
                hit1 = 1
            if self.longmai.get_distance() in card2.range:
                hit2 = 1
            # 对战结算
            result_number = card1.attribute.value - card2.attribute.value
            if hit1 == 1 and hit2 == 1:
                if result_number == -1 or result_number == 2:
                    hit1 = 1
                    hit2 = 0
                elif result_number == -2 or result_number == 1:
                    hit1 = 0
                    hit2 = 1
        elif isinstance(card1, Action):
            # 范围结算
            if self.longmai.get_distance() in card1.range:
                hit1 = 1
                hit2 = 0
            else:
                hit1 = 0
                hit2 = 1
        elif isinstance(card2, Action):
            if self.longmai.get_distance() in card2.range:
                hit1 = 0
                hit2 = 1
            else:
                hit1 = 1
                hit2 = 0
        else:
            hit1 = 0
            hit2 = 0
        # 1号的伤害结算
        if hit1 == 1 and isinstance(card1, Action):
            damage = card1.damage + card1.bonus[self.longmai.get_longmai()[card1.attribute.value] - 1] + fighter1.bonus[card1.attribute.value]
            return Result(1, damage, card1.attribute, card1.longmai_change)
        elif hit1 == 1 and not isinstance(card1, Action):
            return Result(1, 0, Skill.MOVE, 2)
        # 2号的伤害结算
        elif hit2 == 1 and isinstance(card2, Action):
            damage = card2.damage + card2.bonus[self.longmai.get_longmai()[card2.attribute.value] - 1] + fighter2.bonus[card2.attribute.value]
            return Result(2, damage, card2.attribute, card2.longmai_change)
        elif hit2 == 1 and not isinstance(card2, Action):
            return Result(2, 0, Skill.MOVE, 2)
        else:
            return

            
            