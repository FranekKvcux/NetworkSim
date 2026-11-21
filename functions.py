def encode_packet(from_id, to_id, message):
    data = message.encode("utf-8")

    packet = bytes([
        int(to_id),
        int(from_id),
        len(data)
    ]) + data
    return packet

def decode_packet(packet):
    to_id = packet[0]
    from_id = packet[1]
    length = packet[2]
    data = packet[3:3 + length].decode("utf-8")
    return to_id, from_id, data 