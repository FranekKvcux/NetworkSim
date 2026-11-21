def stringtobin(string: str):
    return " ".join(f"{byte:08b}" for byte in string.encode("utf-8"))

def bintostring(binary: str):
    bits = binary.split()
    return bytes(int(byte, 2) for byte in bits).decode("utf-8")