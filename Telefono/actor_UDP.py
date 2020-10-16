
import socket
IpAddress = '192.168.0.118' #0.0.0.0(Mio)
port = 7000

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv.bind((IpAddress,port))

#ricezione del messaggio
data, address = srv.recvfrom(8036)
data= data.decode()
print(f"msg from client: {data} ,  address {address} ") 

srv.close()

#inviare

server_Ip = '192.168.0.128' #Giave(Prossimo)
server_port = 7000

cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#invio del messaggio
cli.sendto(data.encode(),(server_Ip,server_port))

data = cli.recv(8036)

cli.close()

