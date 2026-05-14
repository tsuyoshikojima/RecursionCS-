import os
import socket

# ストリーム型のUNIXドメインソケットを作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# IPCではIPアドレスやポート番号の代わりにファイルパスを使用
server_address = "/tmp/socket_file"

# 前回の実行時にソケットファイルが残っている場合に削除する
try:
    os.unlink(server_address) # ファイルパスを削除する。os.remove()と同じ
except FileNotFoundError:
    pass

print(f"Starting up on {server_address}")

# このサーバー側のソケットをファイルパスに紐付ける
# これによってクライアント側が接続先サーバーのソケットを識別することができる。
sock.bind(server_address)

# ソケットを接続待ち状態にする
sock.listen(1)

while True:
    # データ送受信用の新しいソケットオブジェクト
    connection, client_address = sock.accept()

    try:
        while True:
            # 最大16バイトのbytes型のデータを受信する
            # 空のbytes型オブジェクト b'' が返ってきた場合、クライアントの接続が切れたことを示す
            data = connection.recv(16)

            if data:
                data_str = data.decode("utf-8")
                print("Received " + data_str)

                response = "Processing " + data_str
                connection.sendall(response.encode("utf-8"))
            else:
                print("no data from client", client_address)
                break

    finally:
        print("Closing current connection")
        connection.close()