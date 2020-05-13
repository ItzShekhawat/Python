import socket

ip = '127.0.0.1'
host = 80
indirizzo = (ip,host)

sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sok.connect(indirizzo)

msg = input("Insert your massage : ")
sok.sendall(msg.encode())
data = sok.recv(4096)
print(data.decode())

sok.close()



    