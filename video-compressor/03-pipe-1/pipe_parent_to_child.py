import os

# パイプを作成
# r:読み取り専用
# w:書き込み専用
r, w = os.pipe()

pid = os.fork()

if pid > 0:
    # 親プロセスは、書き込むだけなので読み取り端は閉じる
    os.close(r)

    message = f"Message from parent with pid {os.getpid()}"
    print(f"Parent, sending out the message - {message}")

    # 文字列をバイト列にして書き込む
    os.write(w, message.encode("utf-8"))

    os.close(w)

elif pid == 0:
    os.close(w)

    print(f"Fork is 0, this is a child PID : ", os.getpid())

    with os.fdopen(r) as f:
        print("Incoming string : ", f.read())