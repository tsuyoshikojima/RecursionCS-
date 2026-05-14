import sys
import socket

# UNIXドメインソケットを作成する
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = "/tmp/socket_file"
print(f"connecting to {server_address}")

try:
    # サーバー側のソケットに接続する
    sock.connect(server_address)
except OSError as err:
    print(err)
    sys.exit(1)

try:
    message = "Sending a message to the server side"

    sock.sendall(message.encode("utf-8"))

    sock.settimeout(2)

    try:
        while True:
            data = sock.recv(32)

            if not data:
                break

            print("Server response: " + data.decode("utf-8"))

    except TimeoutError:
        print("Socket timeout, ending listening for server messages")

finally:
    print("closing client socket")
    sock.close()