import socket

ip = '127.0.0.1'
host = 80
indirizzo = (ip,host)

sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sok.bind(indirizzo)
sok.listen(3)

conn , address = sok.accept()
print(f'Connect by : {address} ')
dato = conn.recv(4096)
conn.sendall(dato)

sok.close()


