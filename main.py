import functions as fn
from server import Server
from client import Client

# MAX IDes: 10 (0-9)

# TO DO:
#  - send "hello" from Phone1 to Phone2

srvr = Server("Server1", '0')
clnt1 = Client("Phone1", '1')
clnt2 = Client("Phone2", '2')

data_bus = clnt1.send("hello", '0', '2')
srvr.read(data_bus)