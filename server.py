import functions as fn
from client import Client
class Server:
    def __init__(self, name: str, id: int, clients:list[Client]):
        self.name = name
        self.id = id
        self.clients = clients

    def read_and_send(self, packet):
        to_id, from_id, data = fn.decode_packet(packet)
        client = next((c for c in self.clients if c.id == to_id), None)
        client.recive(from_id, data)