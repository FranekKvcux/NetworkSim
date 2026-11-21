import functions as fn
class Client:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def send(self, data, to: int):
        return fn.encode_packet(self.id, to, data)

    def recive(self, from_id, data):
        print(f"{self.id}: Recived from {from_id}: {data}")