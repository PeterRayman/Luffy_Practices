def person_info(name , age ,gender = "女"):
    print(f"姓名：{name} , 年龄：{age} , 性别：{gender}")

person_info("Yinger" , 16 )#使用位置参数和默认参数
person_info("Longer" , 18 , "男")#用位置参数替换了默认参数

#可变参数使用*来标记。
def meet_person(meet_name , *person_name):

    print(f"""
    本次会议的名称是：{meet_name},
    本次会议的与会领导有：{person_name}
     """)
meet_person("世界宣教大会","Yinger","Longer","Peter","POLO")