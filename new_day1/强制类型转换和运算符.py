num = 3.5
print(type(num) , num)
#强制类型转换
num = int(num)
print(type(num) , num)


a = 9.9
b = 13
c = 30.5

#注意浮点型在内存中存储不精确，最好不要进行==,<=,>=的比较运算
#print(a>=c)