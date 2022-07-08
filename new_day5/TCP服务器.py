from socket import *

ser_socket = socket(AF_INET , SOCK_STREAM) #创建TCP协议的服务器端套接字对象,只负责连接客户端
ser_socket.bind(("192.168.2.110" , 60000)) #给套接字对象绑定地址和端口
ser_socket.listen(5) #设置最大挂起连接队列长度

#等待客户端连接，获得两个返回值：1.一个用来执行连接后具体收发操作的新socket对象；2.客户端地址和端口
new_socket , client_addr = ser_socket.accept()
print(f"已经与客户端{client_addr[0]}:{client_addr[1]}建立连接。。。")

#建立连接之后接收信息
recv_data = new_socket.recv(1024) #收到的不再是元组，因为安全连接不需要再在信息中附带地址和端口。
print("收到客户端发来的消息：{0}".format(recv_data.decode()))

#接受消息之后再回复消息
new_socket.send(input("向客户端回复消息：").encode()) #安全连接，不需要再指定对方地址和端口

#关闭socket对象 先关accept新生成的，再关建立服务器时创建的
new_socket.close()
ser_socket.close()