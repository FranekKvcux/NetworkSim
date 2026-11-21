import functions as fn
from client import Client
class Server:
    def __init__(self, name: str, id: int, clients:list[Client]):
        self.name = name
        self.id = id
        self.clients = clients

    def read(self, data_bin: str):
        pass