**CLIENT-SERVER communicator**
<hr>

**Description**<br>
Simple CHAT-BOX which uses only standard libraries of Python 3.7, including sockets, threading and tkinter.
You can find f-strings here, so is important to have Python 3.7.


**Environment**<br>
The project does not require external libraries, so you don't have to install any requirements and create environment.
But if you want to, look at instructions below:

create:<br>
`virtualenv -p python3.7 <your_env_name>`<br>
activate:<br>
`source <your_env_name>/bin/activate`

If you have activated environment, you can install other libraries by `pip install <libraryname>` to improve this project. 



**Running**<br>
First, you have to run SERVER.py. Enter your directory and type:<br>
`python3.7 SERVER.py`<br>
You can choose PORT number or press enter, script has default port number (15000). After this, 
server is waiting for connections from other clients.

Now, you can run CLIENT.py. After running this script, you have to type PORT number (is important to type the same value 
in both scripts, for server and for all clients)

If you type the same ports, GUI window will open and you can give username for your Client.<br>
On your GUI window you will see your username and your ip address (it can be localhost also) and you can send messages.

I encourage to copy Client.py script to other file, and run it. Look at server communications (in terminal and chat window).
Now you can try simulate chat between two or more clients of chat-server.

