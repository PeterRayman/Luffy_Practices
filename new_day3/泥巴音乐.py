"""
需求：制作一个音乐播放小程序
在指定时间，随机从音乐文件夹中播放音乐
"""
import pygame   #导入pygame模块，使用其中的音乐播放功能
import random   #导入random模块，实现随机播放音乐
import time     #导入time模块，调取系统时间，实现定时播放
import os       #导入os模块，使用系统的文件和目录相关功能

#定义一个实现播放音乐功能的函数 参数：音乐文件路径
def play_music(file):
    pygame.mixer.init() #初始化混音器
    pygame.mixer.music.load(file)   #混音器读取音乐文件
    pygame.mixer.music.play()   #混音器开始播放音乐文件
    time.sleep(20)  #持续播放20秒
    pygame.mixer.music.stop()   #混音器结束播放音乐文件

#定义一个播放随机音乐的函数，无参数。
def shuffle_play():
    music_list = os.listdir(r"D:\Music")    #获取文件夹下的全部文件名，放入一个列表
    random.shuffle(music_list)  #将音乐列表随机打乱
    file = r"D:\Music/" + random.choice(music_list) #随机选择一首歌曲，形成文件路径
    play_music(file) #播放随机选出的音乐文件

#定义一个播放指定音乐的函数，无参数。
def specific_play():
    file = r"D:\Music/泡沫.mp3" #r为取消转义字符
    play_music(file)

#定义一个程序的启动主函数
def main():
    print("**********本程序由~泥巴君龙儿~制作**********")
    print("------------定时音乐播放系统启动------------")
    while True:
        os_time = time.strftime("%H:%M:%S") #获取当前的系统时间
        time.sleep(0.8) 
        print(f"当前的系统时间是：{os_time}" , end = "\r")  #实现不换行刷新的效果
        # print("\r当前的系统时间是：" , os_time , end = "") #实现的效果与上一行一样

        if os_time == "03:00:00":
            specific_play()
            # break #可以选择跳出循环
        if os_time == "03:02:00":
            shuffle_play()
            # break #可以选择跳出循环

main()