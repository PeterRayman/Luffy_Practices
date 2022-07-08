#导入时间工具库
import time 
#导入pygame工具库
import pygame

print("欢迎使用本程序")

#使用time库中的sleep（）休眠功能，休眠1秒
time.sleep(1)

print("音乐播放系统已开启---")
time.sleep(1.5)
print("***************华丽的分割线*************") 

pygame.mixer.init()
pygame.mixer.music.load(r"D:\苦路.mp3")
pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.music.stop()