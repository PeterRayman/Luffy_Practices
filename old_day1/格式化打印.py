#需求：问用户姓名、年龄、工作、爱好，然后打印成好看的格式

person_info =[]
person_info.append(input("姓名："))
person_info.append(input("年龄："))
person_info.append(input("工作："))
person_info.append(input("爱好："))

print()
print(f"info of {person_info[0]}".center(33 , "-") , end="\r")
print(f"""
Name:{person_info[0]}
Age:{person_info[1]}
Job:{person_info[2]}
Hobbie:{person_info[3]}
----------------end---------------
""")