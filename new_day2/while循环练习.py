import time
num = 10
while num > 0:
    print(f"还有{num}秒进入战斗！")
    time.sleep(1)
    num -= 1
print("*******华丽丽的分割线*******")

hp = 10
while hp >0:
    print(f"怪物剩余血量为:{hp}点！")
    print("怪物攻击玩家！~")
    time.sleep(1)
    print("玩家回击怪物！~")
    hp -= 2
    print("###############")
print("怪物被干掉！玩家获得胜利！~") 