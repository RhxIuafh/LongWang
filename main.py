from utils.fighter import Fighter
from controller.longwang import Distance, Dice, LongMai, Skill
from controller.gameController import GameController
from utils.result import Result

def print_status(red, green, blue, distance, health1, bonus1, health2, bonus2):
    print("---------------龙王·龙脉斗技------------------")
    print("当前斗气: ")
    print("RED: ", red, "GREEN: ", green, "BLUE: ", blue)
    print("当前距离：")
    print("Distance: ", distance)
    print("Fighter1状态:")
    print("血量：", health1)
    print("龙脉加成", bonus1)
    print("Fighter2状态:")
    print("血量：", health2)
    print("龙脉加成", bonus2)

if __name__ == "__main__":
    longmai = LongMai([3,3,3], Distance.MID)
    gameController = GameController(longmai)
    fight1 = Fighter(10, [1,1,1], [0,0,0])
    fight2 = Fighter(10, [1,1,1], [0,0,0])
    while(1):
        # 打印状态
        print_status(gameController.longmai.longmai[Dice.RED.value], 
                    gameController.longmai.longmai[Dice.GREEN.value], 
                    gameController.longmai.longmai[Dice.BLUE.value], 
                    gameController.longmai.get_distance(), 
                    fight1.health, 
                    fight1.bonus, 
                    fight2.health, 
                    fight2.bonus)
        print("1号玩家选择什么操作:1.前进；2.后退；3.突袭；4.强袭；5.狙击；6.爆裂射击；7.古典咏唱；8.新式咏唱")
        ipt = input()
        if ipt == "1":
            card1 = fight1.advance()
        elif ipt == "2":
            card1 = fight1.back()
        elif ipt == "3":
            card1 = fight1.stone1()
        elif ipt == "4":
            card1 = fight1.stone2()
        elif ipt == "5":
            card1 = fight1.scissor1()
        elif ipt == "6":
            card1 = fight1.scissor2()
        elif ipt == "7":
            card1 = fight1.cloth1()
        elif ipt == "8":
            card1 = fight1.cloth2()
        print("2号玩家选择什么操作:1.前进；2.后退；3.突袭；4.强袭；5.狙击；6.爆裂射击；7.古典咏唱；8.新式咏唱")
        ipt2 = input()
        if ipt2 == "1":
            card2 = fight2.advance()
        elif ipt2 == "2":
            card2 = fight2.back()
        elif ipt2 == "3":
            card2 = fight2.stone1()
        elif ipt2 == "4":
            card2 = fight2.stone2()
        elif ipt2 == "5":
            card2 = fight2.scissor1()
        elif ipt2 == "6":
            card2 = fight2.scissor2()
        elif ipt2 == "7":
            card2 = fight2.cloth1()
        elif ipt2 == "8":
            card2 = fight2.cloth2()

        print("结算!")
        gameController.distance_settle(card1, card2)
        result = gameController.damage_settle(card1, card2, fight1, fight2)
        if result is not None:
            print(result.hit, result.damage, result.attribute, result.longmai_change)

            # 受伤阶段
            if result.hit == 1:
                fight2.health -= result.damage
                if fight2.health <= 0:
                    print("1号玩家胜利")
                    exit()
                # 调整龙脉
                print("1号玩家是否调整龙脉Y/N", result.attribute, "+-", result.longmai_change)
                isnotChange = input()
                if isnotChange == "Y" or  isnotChange == "y":
                    if result.attribute is not Skill.MOVE:
                        print("增加或减少龙脉?+/-")
                        addOrDecade = input()
                        if addOrDecade == "+":
                            longmai = gameController.longmai.get_longmai()
                            longmai[result.attribute.value] += result.longmai_change
                            gameController.longmai.set_longmai(longmai)
                        else:
                            longmai = gameController.longmai.get_longmai()
                            longmai[result.attribute.value] -= result.longmai_change
                            gameController.longmai.set_longmai(longmai)
                    else:
                        print("增加什么龙脉? 1.RED;2.GERRN;3.BLUE")
                        whatToAdd = input()
                        if whatToAdd == "1":
                            print("增加或减少龙脉?+/-")
                            addOrDecade = input()
                            if addOrDecade == "+":
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.RED.value] += result.longmai_change
                                gameController.longmai.set_longmai(longmai)
                            else:
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.RED.value] -= result.longmai_change
                                gameController.longmai.set_longmai(longmai)
                        elif whatToAdd == "2":
                            print("增加或减少龙脉?+/-")
                            addOrDecade = input()
                            if addOrDecade == "+":
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.GREEN.value] += result.longmai_change
                                gameController.longmai.set_longmai(longmai)
                            else:
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.GREEN.value] -= result.longmai_change
                                gameController.longmai.set_longmai(longmai)
                        elif whatToAdd == "3":
                            print("增加或减少龙脉?+/-")
                            addOrDecade = input()
                            if addOrDecade == "+":
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.BLUE.value] += result.longmai_change
                                gameController.longmai.set_longmai(longmai)
                            else:
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.BLUE.value] -= result.longmai_change
                                gameController.longmai.set_longmai(longmai)   
                        
                else:
                    print("不调整龙脉")
                    
            if result.hit == 2:
                fight1.health -= result.damage
                if fight2.health <= 0:
                    print("2号玩家胜利")
                    exit()
                print("2号玩家是否调整龙脉Y/N", result.attribute, "+-", result.longmai_change)
                isnotChange = input()
                if isnotChange == "Y" or  isnotChange == "y":
                    if result.attribute is not Skill.MOVE:
                        print("增加或减少龙脉?+/-")
                        addOrDecade = input()
                        if addOrDecade == "+":
                            longmai = gameController.longmai.get_longmai()
                            longmai[result.attribute.value] += result.longmai_change
                            gameController.longmai.set_longmai(longmai)
                        else:
                            longmai = gameController.longmai.get_longmai()
                            longmai[result.attribute.value] -= result.longmai_change
                            gameController.longmai.set_longmai(longmai)
                    else:
                        print("增加什么龙脉? 1.RED;2.GERRN;3.BLUE")
                        whatToAdd = input()
                        if whatToAdd == "1":
                            print("增加或减少龙脉?+/-")
                            addOrDecade = input()
                            if addOrDecade == "+":
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.RED.value] += result.longmai_change
                                gameController.longmai.set_longmai(longmai)
                            else:
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.RED.value] -= result.longmai_change
                                gameController.longmai.set_longmai(longmai)
                        elif whatToAdd == "2":
                            print("增加或减少龙脉?+/-")
                            addOrDecade = input()
                            if addOrDecade == "+":
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.GREEN.value] += result.longmai_change
                                gameController.longmai.set_longmai(longmai)
                            else:
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.GREEN.value] -= result.longmai_change
                                gameController.longmai.set_longmai(longmai)
                        elif whatToAdd == "3":
                            print("增加或减少龙脉?+/-")
                            addOrDecade = input()
                            if addOrDecade == "+":
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.BLUE.value] += result.longmai_change
                                gameController.longmai.set_longmai(longmai)
                            else:
                                longmai = gameController.longmai.get_longmai()
                                longmai[Dice.BLUE.value] -= result.longmai_change
                                gameController.longmai.set_longmai(longmai)   
                else:
                    print("不调整龙脉")

