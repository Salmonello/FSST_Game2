import socket, threading

HEADER = 600
PORT = 5050
SERVER = socket.gethostbyname("0.0.0.0")
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
print("SERVER: ", SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

#opens always a new thread if a new connection apears
def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        clients.append(conn)

#Handls a client connection and calls the msg_client.handl
def handle_client(conn:socket.socket, addr:tuple):
    print(conn)
    connected = True
    try:
        print(f"[ACTIVE CONNECTION] {threading.active_count() -1 }\n")
        while connected:
            msg = conn.recv(HEADER)
            for client in clients:
                if client != conn:
                    client.send(msg)
                
    except ConnectionResetError:
        clients.remove(conn)
    conn.close()

if __name__ == "__main__":
    start_server()