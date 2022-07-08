import  tkinter as tk

from pygame import GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH	#使用as来改别名，方便之后频繁调用该模块，该别名后只能使用别名调用

window = tk.Tk()	#创建一个静态的主窗口（无显示效果）
window.title("我的主窗口")		#给窗口设置标题
window.geometry("720x360")	#给窗口设置大小，单位为像素，中间乘号为英文小写x

var = tk.StringVar()    #定义一个tkinter中的字符串变量对象。
var.set("Hello World ！")   #用set函数对该字符串变量进行赋值。
#在本窗口中创建一个标签
l = tk.Label(window , textvariable=var , bg = "Violet" , font=("仿宋",14) , width=30 , height=3)
#文本参数为变量就不能用text，而要用textvariable
l.pack()	#以默认情况安置此标签

hit = 0
def hit_me():
    global hit
    if hit == 0:
        var.set("亢龙有悔！")
        hit = 1
    elif hit ==1:
        var.set("飞龙在天！")
        hit = 2
    elif hit == 2:
        var.set("龙战于野！")
        hit = 3
    else:
        var.set("双龙出海！")
        hit = 0

#tkinter中的按钮组件，使用command参数来指定按下按钮所调用的函数功能，函数不需要加括号。
b = tk.Button(window , text="降龙十八掌" , font=("黑体",12) , bg="Green" , width=20 , height=2 , command=hit_me)
b.pack()

#tkinter中的单行文本输入域组件
e1 = tk.Entry(window , show=None , font=("仿宋" , 12))  #文本为默认明文输入
e1.pack()
e2 = tk.Entry(window , show="*")    #文本为密文输入
e2.pack()

window.mainloop()	#让窗口不断刷新以呈现效果。