import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_serv = "192.168.0.118"
port_serv = 7000
add = (ip_serv, port_serv)
s.bind(add)

msg_bytes, address = s.recvfrom(2048)
msg = msg_bytes.decode()

print(f"Connected to : {address} and recived {msg} : ")

s.sendto(msg.encode(), address)
   
s.close()