info_list = ["龙儿", 18 , 180 , "爱吃西瓜", 180]
mess_list = ["莹儿","泥巴君", "小白" , 234.56]

print(info_list[0])#角标从0开始
print(mess_list[-1])#也可以倒着访问角标

#替换列表中的元素
info_list[3] = "爱吃草莓"
print(info_list)

#添加元素 append()方法把会新元素添加到末尾
info_list.append("学习Pyrhon中")
print(info_list)

#在指定位置添加新元素（插入新元素）
info_list.insert(2,"喵了一个胖")
print(info_list)

#合并（拼接）列表
full_list = info_list + mess_list
print(full_list)

#删除列表中的指定元素
info_list.remove(180)#通过值来删除元素，如果有多个相同值的元素，删除发现的第一个元素
print(info_list)
pop_name = mess_list.pop(2)#通过下标来确定要删除的元素,方法会返回被删除元素的值。
print(mess_list)
print(pop_name)

#将字符串分割成列表(字符串类型的方法)
str1 = "1,2,3,4,5"
str_list = str1.split(",")#按照指定的条件，将字符串分割成列表
print(str_list)

#将列表糅合成字符串（也是字符串类型的方法，因此列表中元素也得是字符串类型，其它类型无法拼接成字符串）
join_list = ["张三","李四","王五"]
str2 = "+".join(join_list)#按照指定的连接字符将列表中元素揉合成字符串,列表中的各元素也得是字符串类型
print(str2)