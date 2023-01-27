import socket

HEADER = 600
PORT = 5050
FORMAT = 'utf-8'
DISCONNET_MASSAGE = "bye"
SERVER = "localhost"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg:bytes):
    msg_length = str(len(msg))
    message = msg_length.encode(FORMAT) + b" " * (HEADER - len(msg_length))
    message += msg
    client.send(message)

def recif() -> bytes:
    msg_length = client.recv(HEADER).decode(FORMAT)
    print(msg_length)
    msg = client.recv(int(msg_length))
    return msg