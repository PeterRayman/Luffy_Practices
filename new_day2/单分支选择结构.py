hp = 10000
mp = 5000

if hp >3000 and mp > 2000 :
    print("开启隐藏关卡！")
    print("出现精英BOSS！")

print("游戏继续********")

#成员运算符in
play_list = ["Yinger" , "Longer" , "xiaobai" , "nibajun" , "Peter" , "POLO"]

if "Yinger" in play_list:
    print("在成员中！")

if "Miao" not in play_list:
    print("不在成员中！")

print("程序继续################")

#input()方法，接收到的默认为字符串。
print("猜数字游戏：")
p_num = float(input("请输入你猜测的数字："))#将获取来的字符串强制类型转换为浮点数
if p_num == 7:
    print("恭喜你，猜对了！")

import time
time.sleep(2)
print("游戏结束！")