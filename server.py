import socket, threading


PORT = 5052
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 2048
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)





def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr}')

    while True:
        rec_full_msg = conn.recv(HEADER).decode(FORMAT)
        rec_name = rec_full_msg[:rec_full_msg.find(':')]
        rec_msg = rec_full_msg[rec_full_msg.find(':') + 1:]

        if rec_msg == '!disconnect':
            break
        else:
            send_msg = rec_full_msg
            conn.sendall(send_msg.encode(FORMAT))

    print(f'[LOST CONNECTION] {addr} name:{rec_name}')
    conn.close()


def start():
    server.listen()
    print(f'[LISTENING] server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')  # .active_count() returns the no. of threads; -1 just for *our* convenience nvm that


print('[STARTING] server is starting...')
start()
