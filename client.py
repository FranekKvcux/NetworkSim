import functions as fn
class Client:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

    def send(self, data, srvr_id: str, addr_id: str):     # data, server_id, addressee_id
        all_string = f"{srvr_id}{addr_id}{self.id}{data}"               # SRVR_ID ADDR_ID SNDR_ID DATA
        rdy_to_snd = fn.stringtobin(all_string)
        print(f"Send: {rdy_to_snd}")
        return rdy_to_snd
