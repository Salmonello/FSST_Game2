from network import *
import socket, threading
import handle_comands

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname("0.0.0.0")
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNET_MASSAGE = "bye"
print("SERVER: ", SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#opens always a new thread if a new connection apears
def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    net_id=0
    while True:
        conn, addr = server.accept()
        network = Network(conn, addr)
        thread = threading.Thread(target=handle_client, args=(network, net_id))
        thread.start()
        net_id += 1
        print(f"[ACTIVE CONNECTION] {threading.active_count() -1 }\n")

#Handls a client connection and calls the msg_client.handl
def handle_client(client:Network, net_id:int):
    connected = True
    handle_comands.set_network(net_id, client)
    try:
        while connected:
            msg = client.conn.recv(HEADER).decode(FORMAT)
            if msg:
                if msg == DISCONNET_MASSAGE:
                    connected = False
                    # bei disconnect            TODO
                else:
                    print(msg)
                    handle_comands.handle_commands(msg, net_id)
                
    except ConnectionResetError:
        pass    #                               TODO
    client.conn.close()

if __name__ == "__main__":
    print("[STARTING] server startet")
    start_server()