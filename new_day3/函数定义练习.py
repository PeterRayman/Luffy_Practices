from tkinter import N


def sum():
    num = 0
    for i in range(1 , 101):
        num += i
    print(num)

sum()

def num_max(a , b):
    if a >= b:
        return a
    else:
        return b

max = num_max(5, 7)
print(max)

def my_list():
    return 1,2,3,4,5

z,x,c,v,b = my_list()
print(z,x,c,v,b)

k = my_list()
print(k)

#注意函数内外变量的作用域
m = 10
def demo1():
    m = 20
    print(m)
demo1()
print(m)

#在函数内使用global关键字声明使用函数外的全局变量
n = 10
def demo2():
    global n #先声明使用的是函数外的全局变量
    n = 20 #再进行使用操作
    print(n)
demo2()
print(n)