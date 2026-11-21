import functions as fn
from server import Server
from client import Client

# TO DO:
#  - send "hello" from Phone1 to Phone2

srvr = Server("Server1", 0)
clnt1 = Client("Phone1", 1)
clnt2 = Client("Phone2", 2)