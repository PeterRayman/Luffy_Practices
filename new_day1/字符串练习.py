#字符串拼接
name = "龙儿"
age = 18
message = "喜欢吃西瓜"

print(name + str(age) + message)

message1 = "莹儿喜欢吃草莓"
#字符串切片 角标从0开始计数 切片“顾头不顾尾”。
print(message1[2:4])
#len(str)函数返回字符串的长度，从1开始计数。
print(message1[2 : len(message1)])#顾头不顾尾，否则要-1，不然超范围报错

#字符串格式化输出
name1 = "小白"
print(f"狗狗的名字叫：{name1}")

#转义字符
print("打印反向斜杠\\,打印双引号\"\"。")#要注意引号配对

#三引号可以保存字符串编写格式
message2 = """
锄禾日当午，
    床前明月光，
        给我一个酸菜的缸，
            腌透悲伤！
                 ————————李小白
"""
print(message2)