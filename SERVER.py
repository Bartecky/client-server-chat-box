#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

#  setting variables, creating socket
clients = {}
addresses = {}
messages = []

HOST = ""
PORT = input("Enter port: ")

if not PORT:
    PORT = 15000
else:
    PORT = int(PORT)

ADDRESS = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDRESS)


def accepting_connections():
    """
    Waiting for incoming connections
    """
    while True:
        client, address = SERVER.accept()
        print(f"{address[0]} has connected")
        addresses[client] = address
        client.send(bytes("Type your name and press enter!", "utf8"))
        Thread(target=get_client, args=(client, address)).start()


def get_client(client, address):
    """
    Main function of chat-box
    """
    name = client.recv(1024).decode("utf8")
    username = f"{name}@{address[0]}"  # username without port number
    welcome_msg = f"Welcome {username}, nice to see you! Press 'closeapp' to quit"
    client.send(bytes(welcome_msg, "utf8"))
    if messages:
        print('Previous messages:\n' + '\n'.join(messages))

    msg = f"{username} has joined!"
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(1024)
        if msg != bytes("closeapp", "utf8"):
            broadcast(msg, f"{username}: ")
            msg = f"{username}: {msg.decode()}"
            messages.append(msg)
        else:
            client.send(bytes("closeapp", "utf8"))
            print(f"{username} has left the chat")
            client.close()
            del clients[client]
            broadcast(bytes(f"{username} has left the chat.", "utf8"))
            break


def broadcast(msg, prefix=""):
    """
    Generate messages for all clients
    """
    for client in clients:
        client.send(bytes(prefix, "utf8") + msg)


if __name__ == "__main__":
    SERVER.listen(50)  # up to 50 connections
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accepting_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
