import time 
for i in range(10):
    print(i)
    time.sleep(1)
print("######################")

#range函数的参数顾头不顾尾，步长
for i in range(1,10,2):
    print(i)
    time.sleep(1)
print("######################")

#求1-100当中奇数的和
sum = 0
for i in range(1,101):
    if i % 2 != 0:
        sum += i
print(sum)
print("################")

name_list = ["Yinger" , "Longer" , "xiaobai" , "nibajun" , "Peter" , "POLO"]
for name in name_list:
    print(f"""
    亲爱的{name}:
        欢迎您莅临本单位指导！
            欢迎您提出宝贵意见和建议。


    """)