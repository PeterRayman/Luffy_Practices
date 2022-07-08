from socket import *    #从socket模块中导入所有的工具

#   s = socket.socket(socket.AF_INET , socket_DGRAM)
s = socket(AF_INET , SOCK_DGRAM) #创建socket对象，简写形式 使用ipv4协议和UDP协议

addr = ("192.168.2.110" , 2425) #接收方的ip地址和接收数据端口
data = "1:123456:莹儿:莹儿的小本本:32:喜欢龙儿咧" #要发送的数据，不同程序的格式各不相同

#使用socket对象来向接收方发送数据，使用UDP协议的套接字对象上之sendto方法来发送数据，参数为数据，以及记录目标地址和端口的元组
s.sendto(data.encode("gb2312") , addr) #数据在网络中只能转换成字节来发送，而且双方的编码格式要一致
s.close()#使用完毕需要关闭socket对象
