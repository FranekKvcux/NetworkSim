def encode_packet(from_ip, to_ip, message):
    data = message.encode("utf-8")

    packet = bytes([
        int(to_ip),
        int(from_ip),
        len(data)
    ]) + data
    return packet

def decode_packet(packet):
    to_ip = packet[0]
    from_ip = packet[1]
    length = packet[2]
    data = packet[3:3 + length].decode("utf-8")
    return to_ip, from_ip, data 