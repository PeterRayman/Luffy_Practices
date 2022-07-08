import random

num1 = random.random()#产生一个0-1之间的随机浮点数
print(num1)

num2 = random.uniform(4 , 7)#产生一个指定范围内的随机浮点数
print(num2)

num3 = random.randint(2 , 15)#产生一个指定范围内的随机整数
print(num3)

a = random.choice("sadfghjkl")#从一个序列中选择出一个随机值
print(a)

list1 = ["Yinger" , "Longer" , "xiaobai" , "nibajun" , "Peter" , "POLO"]
b = random.choice(list1)#序列可以是字符串，也可以是列表等。
print(b)

list2 = [1,2,3,4,5,6,7,8]
random.shuffle(list2)#将列表中元素的顺序随机打乱，但字符串本身无法打乱。
print(list2)

list3 = random.sample(list1 , 3)#从列表中随机选出指定个数的元素形成一个新列表
print(list3)