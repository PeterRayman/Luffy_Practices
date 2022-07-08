from ctypes import windll
import tkinter
from tkinter.font import BOLD
from unittest import result 
import pygame
import random 

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load(r"D:\Music\明明就.mp3")
    pygame.mixer.music.play()

window = tkinter.Tk()
window.title("本程序由泥巴君龙儿倾情无聊制作！远离赌博，珍爱生命！")
window.geometry("600x800")

play_music()

chips = 1000

welcome_l = tkinter.Label(window , text="欢迎使用老虎机游戏" , bg="Gold", fg="Blue" , font=("黑体",28,BOLD) , width=30 , height=3)
welcome_l.grid(column=0 , columnspan=2)

var_chips = tkinter.StringVar()
var_chips.set(f"当前筹码余额为{chips}点")
chips_l = tkinter.Label(window , textvariable=var_chips , bg="Blue", fg="Red" , font=("黑体",28,BOLD) , width=30 , height=3)
chips_l.grid(column=0 , columnspan=2)

chips_down = tkinter.Entry(window , show=None , font=("仿宋 28"))
chips_down.grid(column=0 , columnspan=2 , pady=30)

var_dices = tkinter.StringVar()
var_dices.set("色子点数公布栏")
dices_l = tkinter.Label(window , textvariable=var_dices , bg="Blue", fg="Pink" , font=("黑体",24,BOLD) , width=30 , height=3)
dices_l.grid(column=0 , columnspan=2)

var_result = tkinter.StringVar()
var_result.set("竞猜结果即刻公布")
result_l = tkinter.Label(window , textvariable=var_result , bg="Gold", fg="Green" , font=("黑体",20,BOLD) , width=30 , height=3)
result_l.grid(column=0 , columnspan=2 , pady=30)

#制作一个摇色子生成随机三个点数的功能
def shake_dice():
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

def big():
    global chips
    your_bat = int(chips_down.get())
    if your_bat > chips:
        var_result.set("您没有这么多筹码，请重新输入！")
    else:
        dices = shake_dice()
        points = sum(dices)
        if shake_result(points) == "大":
            var_dices.set(f"本轮色子为：{dices} 共{points}点大！")
            var_result.set(f"恭喜你猜中！本次赢得了{your_bat}点筹码!")
            chips += your_bat
            var_chips.set(f"当前筹码余额为{chips}点")
        else:
            var_dices.set(f"本轮色子为：{dices} 共{points}点小！")
            var_result.set(f"很遗憾猜错了！本次输掉了{your_bat}点筹码！")
            chips -= your_bat
            var_chips.set(f"当前筹码余额为{chips}点")

            if chips == 0:
                var_result.set("你的筹码已经输光了！")
                var_chips.set(f"当前筹码余额为{chips}点")

def small():
    global chips
    your_bat = int(chips_down.get())
    if your_bat > chips:
        var_result.set("您没有这么多筹码，请重新输入！")
    else:
        dices = shake_dice()
        points = sum(dices)
        if shake_result(points) == "小":
            var_dices.set(f"本轮色子为：{dices} 共{points}点小！")
            var_result.set(f"恭喜你猜中！本次赢得了{your_bat}点筹码!")
            chips += your_bat
            var_chips.set(f"当前筹码余额为{chips}点")
        else:
            var_dices.set(f"本轮色子为：{dices} 共{points}点大！")
            var_result.set(f"很遗憾猜错了！本次输掉了{your_bat}点筹码！")
            chips -= your_bat
            var_chips.set(f"当前筹码余额为{chips}点")

            if chips == 0:
                var_result.set("你的筹码已经输光了！")
                var_chips.set(f"当前筹码余额为{chips}点")


b_button = tkinter.Button(window , text="大" , bg="Chocolate" , font=("黑体 28 bold") , width=10 , height=2 , command=big)
s_button = tkinter.Button(window , text="小" , bg="Chocolate" , font=("黑体 28 bold") , width=10 , height=2 , command=small)
b_button.grid(row=6 , column=0 , padx=10 , pady=10)
s_button.grid(row=6 , column=1 , padx=10 , pady=10)

window.mainloop()