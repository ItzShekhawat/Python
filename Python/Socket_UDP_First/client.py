import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_server = ""
server_port = 6000

data = input(">")

s.sendto(data.encode(), (ip_server, server_port))

data , address = s.recvfrom(2048)

msg = data.decode()

print(msg)

s.close()
