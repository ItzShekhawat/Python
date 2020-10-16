import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_server = "192.168.88.87"
server_port = 7000

data = input(">")

s.sendto(data.encode(), (ip_server, server_port))


print(data)

s.close()
