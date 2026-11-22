# NetworkSim

**A lightweight network communication simulator written in Python.**

NetworkSim is a small educational project designed to simulate basic communication between clients through a central server. It demonstrates packet encoding, decoding, message transmission, and a simple client-server architecture.

## Features

- **Client-Server Architecture** – Clients communicate through a central server.
- **Packet Encoding** – Messages are encoded into byte sequences before transmission.
- **Packet Decoding** – The server decodes incoming packets and extracts their contents.
- **UTF-8 Support** – Supports text messages using UTF-8 encoding.
- **Multiple Clients** – Supports communication between multiple registered clients.
- **Lightweight Implementation** – Built entirely with Python and no external dependencies.

## How It Works

Each client has a unique ID and can send messages to other clients through the server.

The communication process:

1. A client creates a message.
2. The message is encoded into a byte packet.
3. The packet is sent to the central server.
4. The server decodes the packet.
5. The server forwards the message to the destination client.

## Packet Structure

Each packet consists of three header fields followed by the message payload.

| Field | Size | Description |
|---|---:|---|
| Destination ID | 1 byte | ID of the receiving client |
| Source ID | 1 byte | ID of the sending client |
| Payload Length | 1 byte | Length of the message in bytes |
| Payload | Variable | UTF-8 encoded message |

## Usage

The main communication function is `send()`.

```python
send(to_id, from_id, data)
```

Example:

```python
send(2, 1, "Hello World")
```

This sends a message from client `1` to client `2` through the server.

## Project Structure

```text
NetworkSim/
│
├── main.py       # Main application and client setup
├── client.py     # Client implementation
├── server.py     # Central server implementation
├── functions.py  # Packet encoding and decoding
│
├── README.md
└── LICENSE
```

## Requirements

- Python 3.9 or newer
- No external dependencies

## Running

Clone the repository:

```bash
git clone https://github.com/FranekKvcux/NetworkSim.git
cd NetworkSim
```

Run the application:

```bash
python main.py
```

## Project Status

NetworkSim is an experimental educational project and is currently under development. Its purpose is to explore basic networking concepts and packet-based communication.

## License

This project is licensed under the **PolyForm Noncommercial License 1.0.0**.

You are free to use, study, modify, and distribute this project for noncommercial purposes. Commercial use is not permitted without separate permission.

See [LICENSE](LICENSE) for details.
