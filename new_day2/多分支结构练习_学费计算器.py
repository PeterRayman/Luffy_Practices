'''
需求：学费计算器
学校共15门可购买课程，每门课程单价：10000；
一次性购买3门课程及以上，每门课程优惠1.5元；
一次性购买5门课程及以上，每门课程优惠2元；
一次性购买10门课程及以上，赠送终身vip，优惠50元，并且送校长签名照。
'''
print("*******学费计算器*******")
num = int(input("请问您要购买几门课程："))

#第一种方法：将判断条件精确化
if 1 <= num <= 2:
    price = num * 10000
    print(f"您需要支付的学费为：{price}元。")
elif 3 <= num <= 4:
    price = (num * 10000) - (num * 1.5)
    print(f"您需要支付的学费为：{price}元。")1
elif 5 <= num <= 9:
    price = (num * 10000) - (num * 2)
    print(f"您需要支付的学费为：{price}元。")
elif 10 <= num <= 15:
    price = (num * 10000) - 50
    print("恭喜你，成为终身vip！")
    print("恭喜你，获得校长签名照一张！")
    print(f"您需要支付的学费为：{price}元。")
elif num > 15:
    print("学校尚未开放这么多门课程，请理性消费！")
else:
    print("您输入的课程数量有误！")

#第二种方法：将判断条件范围最小化，再逐渐放大
if num > 15:
    print("学校尚未开放这么多门课程，请理性消费！")
elif num >= 10:
    price = (num * 10000) - 50
    print("恭喜你，成为终身vip！")
    print("恭喜你，获得校长签名照一张！")
    print(f"您需要支付的学费为：{price}元。")
elif num >= 5:
    price = (num * 10000) - (num * 2)
    print(f"您需要支付的学费为：{price}元。")
elif num >= 3:
    price = (num * 10000) - (num * 1.5)
    print(f"您需要支付的学费为：{price}元。")
elif num >= 1:
    price = num * 10000
    print(f"您需要支付的学费为：{price}元。")
else:
    print("您输入的课程数量有误！")
