from socket import *

while True:
    s = socket(AF_INET , SOCK_DGRAM)
    s.bind(("192.168.2.110" , 9999))
    addr = ("192.168.2.110" , 9998)

    redata = s.recvfrom(1024)
    print("收到的消息：{0}".format(redata[0].decode()))

    data = input("请输入消息：").encode()
    s.sendto(data , addr)
    
    s.close()