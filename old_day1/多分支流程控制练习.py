salary = int(input("请输入你的工资："))

if salary >= 100000:
    print("公司是我家，老板是俺爹！")
elif salary >= 50000:
    print("996是福报！")
elif salary >= 30000:
    print("老板说什么都对！")
elif salary >= 20000:
    print("老板说啥就是啥吧。")
elif salary >= 10000:
    print("老板，我不吭气")
elif salary >= 5000:
    print("老板你咋想的")
elif salary >= 2000:
    print("老板@#￥%")
elif 1999 >= salary >= 0:
    print("老板，俺是恁爹！")
else:
    print("您输入的金额有误！")

#程序由上往下依次运行，当发现一个条件满足就执行，不再往下继续判断，即使之后的条件也满足，也不继续执行
#最后的else，代表当所有的条件都不满足时给出的最后一条路，它不是必须的。但为了保证逻辑的完整性，一般要考虑到写上。

#输入成绩0-100，给出对应的等级A-E
num = int(input("请输入您的成绩（0-100）："))

if 90 <= num <= 100:
    print("您的成绩等级为：A")
elif num >= 80 and num <= 89:
    print("您的成绩等级为：B")
elif num >= 60 and num <= 79:
    print("您的成绩等级为：C")
elif num <= 59 and num >= 40:
    print("您的成绩等级为：D")
elif 39 >= num >= 0 :
    print("您的成绩等级为：E")
else:
    print("您输入的成绩有误！")