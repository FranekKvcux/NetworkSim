import functions as fn
from server import Server
from client import Client

# TO DO:
#  - send "hello" from Phone1 to Phone2

clnt1 = Client("Phone1", 1)
clnt2 = Client("Phone2", 2)
srvr = Server("Server1", 0, [clnt1, clnt2])

clients = {1: clnt1, 2: clnt2}

def send(to_id, from_id, data):
    packet = clients[from_id].send(data, to_id)
    srvr.read_and_send(packet)


send(2, 1, "Hello World1")
send(1, 2, "Hello World2")