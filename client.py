import socket, threading


PORT = 5052
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 2048
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

name = input("Enter your name: ")


def send(msg):
    message = (name + ':' + msg).encode(FORMAT)
    client.sendall(message)


run = True
while run:
    # send_msg = input()
    # send(send_msg)
    send('hi')
    print(client.recv(HEADER).decode(FORMAT))
