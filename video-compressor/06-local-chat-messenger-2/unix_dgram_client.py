import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# sendto()の引数で使用
server_address = "/tmp/unix_dgram_socket_file"

# サーバー側がどのソケットから送られてきたかを識別するのに必要
client_address = "/tmp/unix_dgram_client_socket_file" 

try:
    os.unlink(client_address)
except FileNotFoundError:
    pass

message = "Hello from client"

try:
    sock.bind(client_address)

    # サーバに送信
    print(f"sending {message}")
    sock.sendto(message.encode("utf-8"), server_address)

    # サーバーから受信
    print("waiting to receive")
    bytes_data, address = sock.recvfrom(4096)

    print(f"received {bytes_data.decode('utf-8')}")

finally:
    print("closing socket")
    sock.close()

    try:
        os.unlink(client_address)
    except FileNotFoundError:
        pass

