import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNET_MASSAGE = "by"
SERVER = "192.168.56.1"  #WICHTIG ÄNDERN socket.socket(socket.AF_INET, socket.SOCK_STREAM)------------------------------------------------------------------
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg:str):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
        
def recif():
    while True:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            print(msg)
            #                                               TODO

if __name__ == "__main__":    
    while True:
        send(input())