import functions as fn
from client import Client
class Server:
    def __init__(self, name: str, ip: int, clients:list[Client]):
        self.name = name
        self.ip = ip
        self.clients = clients

    def read_and_send(self, packet):
        to_ip, from_ip, data = fn.decode_packet(packet)
        client = next((c for c in self.clients if c.ip == to_ip), None)
        client.recive(from_ip, data)