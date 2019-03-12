#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import tkinter

#  setting variables, creating socket

HOST = ""
PORT = input("Enter port: ")

if not PORT:
    PORT = 15000
else:
    PORT = int(PORT)

ADDRESS = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDRESS)


def receiving_message():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf8")
            message_list.insert(tkinter.END, message)
        except OSError:
            print('Client probably left the chat')


def sending_message(event=None):
    message = my_message.get()
    my_message.set("")  # input field on GUI
    client_socket.send(bytes(message, "utf8"))
    if message == "closeapp":
        client_socket.close()
        gui.quit()  # close GUI


def closing():
    """
    Closing GUI window
    """
    my_message.set("closeapp")
    sending_message()


# Building GUI

gui = tkinter.Tk()
gui.title("Client-Server ChatBox")

messages_frame = tkinter.Frame(gui)
my_message = tkinter.StringVar()
my_message.set('Type messages here')
scrollbar = tkinter.Scrollbar(messages_frame)
message_list = tkinter.Listbox(messages_frame, height=20, width=60, yscrollcommand=scrollbar.set)

scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(gui, textvariable=my_message)
entry_field.bind("<Return>", sending_message)
entry_field.pack()

send_button = tkinter.Button(gui, text="Send", command=sending_message)
send_button.pack()

gui.protocol("WM_DELETE_WINDOW", closing)

if __name__ == '__main__':
    receive_thread = Thread(target=receiving_message)
    receive_thread.start()
    tkinter.mainloop()
