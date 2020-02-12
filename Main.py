from Window import Window
from Connection import Connection
from GetHost import getHost
import hd


sep = "\x1d"

username = "e"

def formatMessage(m):
    mType,sender,data = m.split(sep)
    return sender+": "+data

def loop():
    for i in window.getEvents():
        connection.send(i,"message",username)
    recieve = connection.getEvents()
    if recieve:
        window._print(formatMessage(recieve))

ip,port = getHost()
username = getHost()
window = Window()
connection = Connection(ip,port)
window.runLoop(loop)