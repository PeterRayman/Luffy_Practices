age_yinger = 16

while True:
    age_guess = int(input("猜猜莹儿芳龄几何："))

    if age_guess > age_yinger:
        print("你胡说，莹儿哪有这么老！")
    elif age_guess < age_yinger:
        print("莹儿虽然很年轻，但也没有这么小啦~")
    else:
        print("猜的没错哦，莹儿永远16岁~")
        break