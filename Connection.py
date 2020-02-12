import socket
class ConnectionError(BaseException): pass
class Connection:
    def __init__(self,ip,port):
        self.s = socket.socket()
        self.s.settimeout(0.1)
        self.host = ip
        self.port = port
        try:
            self.s.connect((self.host, self.port))
        except socket.timeout:
            raise ConnectionError("Could not find host")

    
    def send(self,text,mType,sender):
        sep = "\x1d"
        text = mType+sep+sender+sep+text
        try:
            self.s.send(bytes(text,"UTF-8"))
        except socket.timeout:
            pass
        
    
    def getEvents(self):
        try:
            text = self.s.recv(1026)
            return text.decode("UTF-8")
        except socket.timeout:
            return False
        