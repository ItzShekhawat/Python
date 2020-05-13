import socket
import turtle

ip = '127.0.0.1'
host = 80
indirizzo = (ip,host)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(indirizzo)

    print("Avviato")

    #Variabili per la gestione
    serv = []
    tut = []
    cont = 0
    
    diz = {"F": Forward, "B": Backward, "L": Left, "R": Right}

    while True:
        index = -1

        msg, address = s.recvfrom(4096)
        print(f"Collegamento stabilito con {address}")

        for x in range(len(serv)):
            print("controllo")
            if(serv[x] == (address)):
               index = x
               break 
        

        if (index == -1):
            print("controllo2")
            serv.append(address)
            tut.append(turtle.Turtle())
            index = cont
            cont = cont+1


       # splitto l'input del client 
        
        msg = (msg.decode()).split("_") 
        msg[1] = float(msg[1])
        comm = msg[0]
        value = msg[1]

        #Faccio uscire in caso di richiesta
        if(comm=="Exit"):
            False
        
        

        # eseguo sulla corretta turtle il comando inserito
        #Chiamo il diz delle funzioni inserendi appositi parametri

        diz[comm](tut, index, value)


    s.close()


def Forward(vecT, n, val):
    print("Forward")
    vecT[n].forward(val)

def Backward(vecT, n, val):
    print("Backward")
    vecT[n].forward(val)

def Left(vecT, n, val):
    print("Left")
    vecT[n].left(val)

def Right(vecT, n, val):
    print("Right")
    vecT[n].right(val)


if __name__ == "__main__":
    main()

        
            



