# SOCK_STREAM の通信処理の流れ

## クライアント側

#### 1.ソケットの作成

`socket.socket(family, type)`でsocket objectを生成
アドレスファミリーとソケットタイプを指定

#### 2.サーバーに接続

`socket.connect(address)`

#### 3.データの送受信

`socket.sendall(bytes)`
`socket.recv(bufsize)`

### 4.接続を閉じる

`socket.close()`

## サーバー側

#### 1.ソケットの作成

#### 2.アドレスに紐付け

`socket.bind(adress)`

#### 3.サーバーを有効にし接続を待つ

`socket.listen([backlog])`
システムが新しい接続を拒否するまでに許可する未受付の接続の数を指定する

#### 4.接続を受け付け

`socket.accept()`
戻り値は (conn, address) のペアで、 conn は接続を通じてデータの送受信を行うための 新しい ソケットオブジェクト、 
address は client側のソケットのアドレス

#### 5.データの送受信

#### 6.接続を閉じる


# SOCK_DGRAM の通信処理の流れ

client と server では基本的な処理の部品は同じである。

#### 1.ソケットの作成

#### 2.アドレスへの紐付け

#### 3.データの送受信

`socket.sendto(bytes, address)`
接続レスなので、毎回送信先アドレスを指定。戻り値として送信データのbyteが返ってくる

`socket.recvfrom(bufsize)`
bytes object と 送信元のアドレスが戻り値として渡される。

#### 4.ソケットを閉じる