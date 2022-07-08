from socket import *

client_socket = socket(AF_INET , SOCK_STREAM) #创建TCP协议类型的客户端套接字对象，协议类型要跟客户端一致
client_socket.bind(("192.168.2.110" ， 50000)) #客户端可以不需要绑定，系统自动分配端口。
client_socket.connect(("192.168.2.110" , 60000)) #连接服务器

#连接后向服务器发送信息
client_socket.send(input("向服务器发送消息：").encode()) #安全连接，不需要指定地址和端口

#等待和接收服务器回馈的消息
recv_data = client_socket.recv(1024) #收到的不再是元组
print("收到来自服务器的消息：{0}".format(recv_data.decode())) #把字节流转换成字符来使用。

#别忘了关闭socket对象
client_socket.close()