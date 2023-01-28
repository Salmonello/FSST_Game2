import socket, threading

HEADER = 20
PORT = 5050
SERVER = socket.gethostbyname("0.0.0.0")
ADDR = (SERVER, PORT)
print("SERVER: ", SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADR)

clients = []

#opens always a new thread if a new connection apears
def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        #Waits till client connects
        conn, addr = server.accept()
        #Starts thread to speak to client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        clients.append(conn)

#Handls all messages and redirects them to the other clients
def handle_client(conn:socket.socket, addr:tuple):
    connected = True
    try:
        print(f"[ACTIVE CONNECTION] {threading.active_count() -1 }\n")
        #Server connected with client
        while connected:
            #sends the data from the client to the other client
            msg = conn.recv(HEADER)
            for client in clients:
                if client != conn:
                    client.send(msg)
                
    except ConnectionResetError:
        clients.remove(conn)
    conn.close()

if __name__ == "__main__":
    start_server()