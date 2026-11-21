import functions as fn
class Server:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

    def read(self, data_bin: str):
        data = fn.bintostring(data_bin)
        if data[0] == self.id:
            pass