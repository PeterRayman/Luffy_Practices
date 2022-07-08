#一句代码打印10行“I Love JESUS !”
print("I Love JESUS ！\n" * 10)

#写一个列表，存入6个名字，再把自己的名字插入到Yinger后边
names = ["POLO" , "Peter" , "Yinger" , "泥巴君"]
print(names)
names.insert(3 , "Longer")
print(names)

#把上一个列表中的自己删除掉，然后再追加到列表尾部
print("华丽丽的分割线".center(40 , "*"))
print(names)
#del names[3]
names.remove("Longer")
print(names)
names.append("Longer")
print(names)
