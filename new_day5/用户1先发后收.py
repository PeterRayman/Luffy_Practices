from socket import *

while True:
    s = socket(AF_INET , SOCK_DGRAM)
    s.bind(("192.168.2.110" , 9998)) #给自己绑定ip和端口，“”不写代表默认本机地址
    addr = ("192.168.2.110" , 9999)

    data = input("请输入消息：")
    s.sendto(data.encode() , addr)

    #发送后等待接受回复消息
    redata = s.recvfrom(1024) #参数为指定接受的最大字符量
    print("接收到的消息：{0}".format({redata[0].decode()})) #接收到的是一个元组，第0号元素是消息。

    s.close()