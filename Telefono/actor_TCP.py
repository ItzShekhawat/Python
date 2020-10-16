import socket

def server():
    ip_serv = "192.168.0.118"
    port_serv = 7000
    #addre = (ip_serv, port_serv)

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serv.bind((ip_serv,port_serv))

    serv.listen()

    while True :
        conn, add = serv.accept()

        msg = conn.recv(1024)
        photo = ""
        if len(msg)>0:
            photo = photo+msg

        
    print(f"The connection is {add}, and the message is {msg}")
    
    conn.close()
    client(msg)


def client(msg):
    ip_client = "192.168.0.118"
    port_client = 7000

    addre = (ip_client, port_client)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(addre)

    client.sendall(msg)

    client.close()

if __name__ == "__main__":
    server()