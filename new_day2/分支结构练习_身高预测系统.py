"""
身高预测系统，需求：
身高预测公式：
男性成人时身高 = （父亲身高 + 母亲身高）*0.54
女性成人时身高 = （父亲身高 * 0.923 + 母亲身高）/ 2
如果经常进行体育锻炼，那么可以增加2%
如果有良好的卫生饮食习惯，那么可以增加1.5%
"""
print("********身高预测系统********")
gender = input("请输入孩子的性别(男/女):")
father_h = float(input("请输入父亲的身高(cm):"))
mother_h = float(input("请输入母亲的身高(cm):"))
sport = input("是否经常进行体育锻炼(是/否):")
food = input("是否有uuuuu良好的卫生饮食习惯(是/否):")

if gender == "男":
    child_h = (father_h + mother_h) * 0.54
    if sport == "是":
        child_h *= 1.02
    if food =="是":
        child_h *= 1.015
    print(f"预测身高为：{child_h}")
elif gender == "女":
    child_h = (father_h * 0.923 + mother_h) / 2
    if sport == "是":
        child_h *= 1.02
    if food == "是":
        child_h *= 1.015
    print(f"预测身高为：{child_h}")
else:
    print("孩子性别输入有误！")