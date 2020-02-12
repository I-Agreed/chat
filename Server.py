import socket
import threading
s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 8089
s.bind((host,port))
s.listen(5)
s.settimeout(0.1)
print(f"""Running server:
IP: {host}
Port: {port}""")
sep = "\x1d"
connections = set()


consoleInput = []
def getInput():
    while 1:
        consoleInput.append(input(">"))
inputThread = threading.Thread(target=getInput)
inputThread.start()
def send(text):
    for i in connections:
        try:
            i[0].send(text)
        except socket.timeout:
            pass

def main():
    try:
        c, addr = s.accept()
        c.settimeout(0.1)
        connections.add((c,addr))
        print ("Connection accepted from " + repr(addr[0]))
        #c.send(bytes("Server approved connection\n","UTF-8"))
    except socket.timeout:
        pass
    
    
    for i in connections:
        c = i[0]
        try:
            text = c.recv(1026)
            text = text.decode("utf-8")
            mType,sender,data = text.split(sep)
            if mType == "message":
                send(bytes(text,"UTF-8"))
        except socket.timeout:
            pass
        except ValueError:
            pass
    
    for i in consoleInput:
        if i.startswith("/kick"):
            i = i.split(" ")[1]
            for j in connections:
                if repr(j[0]) == i:
                    j[0].close()

while 1:
    
    main()