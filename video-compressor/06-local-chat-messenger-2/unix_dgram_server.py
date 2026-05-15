import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = "/tmp/unix_dgram_socket_file"

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f"starting up on {server_address}")

sock.bind(server_address)

try:
    while True:
        print("\nwaiting to receive message")

        bytes_data, address = sock.recvfrom(4096)

        print(f"Received {len(bytes_data)} bytes from {address}")
        print(bytes_data.decode("utf-8"))

        if bytes_data:
            sent = sock.sendto(bytes_data, address)
            print(f"sent {sent} bytes back to {address}")

finally:
    print("closing socket")
    sock.close()

    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    