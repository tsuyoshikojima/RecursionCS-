import os
import json

# open()でファイルオブジェクトを返す
with open('config.json', 'r', encoding='utf-8') as f:
    # Pythonのdictとして返される
    config = json.load(f)

fifo_path = config["filepath"]

# 同名のファイルパスが既に存在していた場合削除する
if os.path.exists(fifo_path):
    os.remove(fifo_path)

# 名前付きパイプ用の特殊ファイルを作成
os.mkfifo(fifo_path, 0o600)

print(f"FIFO named {fifo_path} is created successfully.")
print("Type in what you would like to send to clients.")
print("Type 'exit' to quit.")

try:
    while True:
        message = input()

        if message == "exit":
            break

        with open(fifo_path, 'w', encoding="utf-8") as f:
            f.write(message) 
        
finally:
    if os.path.exists(fifo_path):
        os.remove(fifo_path)
