age = int(input("请输入你的年龄："))

if age >=22:
    print("您已经达到法定结婚年龄，可以考虑结婚。")
    marry = input("请问您是否马上结婚（是/否）：")
    if marry == "是":
        print("您已经想好要结婚了呀！恭喜你！")
        wife = input("那么请问您想与哪位女士结婚：")
        if wife == "Yinger":
            print(f"真有眼光呀！{wife}是个完美的选择！")
        elif wife == "Miao":
            print(f"非常的好!{wife}会将你照顾的非常好！")
        elif wife == "xiaobai":
            print(f"{wife}还是一个小宝宝，你咋想的！")
        elif wife == "小红":
            print(f"{wife}的性格太温柔，你要好好保护她！")
        else:
            print("你认识了新欢么，我的天哪！~")
    elif marry == "否":
        print("不考虑马上结婚，那就专心搞事业吧！")
    else:
        print("不知道输入了些啥，可能自己也没想好，回去想吧，再见！")
else:
    print("您还未到法定结婚年龄，滚回去好好学习！")

import time
time.sleep(2)
print("适婚测试程序结束，祝你好运，平安幸福！~")