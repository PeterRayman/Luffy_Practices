"""
需求：
1.摇色子，随机生成三个点数
2.判断三个点数的和是大还是小（3-10为小，11-18为大）
3.用户玩游戏：用户起始有1000点筹码，每一轮用户猜大小，押筹码，如果猜对赢得双倍筹码，如果猜错扣除所押筹码
4.每轮结束用户选择是否结束游戏，或输光筹码自动结束游戏。
"""
import random

#制作一个摇色子生成随机三个点数的功能
def shake_dice():
    print("开始摇色子！")
    dices = []
    for i in range(3):
        dice = random.randint(1,6)
        dices.append(dice)
    return dices

#制作一个判断点数是大是小的功能
def shake_result(points):
    if 11 <= points <= 18:
        return "大"
    else:
        return "小"

#用户玩游戏
def play_game(chips=1000):
    print("**********老虎机小游戏开始**********")
    print("***本程序由泥巴君龙儿倾情无聊制作****")
    print(f"您目前拥有筹码{chips}点。")

    while chips>0:        
        dices = shake_dice()    #开始摇色子
        points = sum(dices)     #加和三个色子的点数
        result_str = shake_result(points)    #获得色子点数大小结果
        results = ["大" , "小"] #结果池
        user_str = input("请选择结果 大/小：")  #玩家选择大小
        if user_str in results:
            chips_down = int(input("请选择下注多少筹码："))
            if chips_down <= chips: #判断每把输入的筹码数不超过总筹码
                if user_str == result_str:  #判断输赢
                    chips += chips_down #赢得筹码
                    print(f"摇出的色子为:{dices}    点数总和为:{points}点   结果为{result_str}!")
                    print(f"恭喜你猜对了！本次赢得了{chips_down}点筹码，现在共有{chips}点筹码。")  
                    user_choice = input("是否进行新一轮游戏 是/否：")
                    if user_choice == "是":
                        print("---------------------------------------------------------")
                        continue
                    elif user_choice == "否":
                        print("见好就收！很好的选择！再见！")
                        break
                    else:
                        print("输入有误！游戏结束！")  
                        break                  
                else:
                    chips -= chips_down #输掉了筹码
                    print(f"摇出的色子为:{dices}    点数总和为:{points}点   结果为{result_str}!")
                    print(f"很遗憾猜错了！本次输掉了{chips_down}点筹码，现在共有{chips}点筹码。")
                    user_choice = input("是否进行新一轮游戏 是/否：")
                    if user_choice == "是":
                        print("---------------------------------------------------------")
                        continue
                    elif user_choice == "否":
                        print("保住了底裤！")
                        break
                    else:
                        print("输入有误！游戏结束！")  
                        break                
            else:
                    print("很抱歉，您没有这么多筹码，请重新开始一轮。")
        else:
            print("您的输入有误，只能选择大或小，请重新输入。")
        print("---------------------------------------------------------")
    else:
        print("筹码不足，游戏结束！远离赌博，珍爱生命！")


play_game()