import os
import json

with open("config.json", 'r', encoding="utf-8") as f:
    config = json.load(f)

fifo_path = config["filepath"]

print("Waiting for messages from server.....")

try:
    while True:
        if not os.path.exists(fifo_path):
            print("FIFO does not exist. Client is exiting.")
            break

        with open(fifo_path, 'r', encoding="utf-8") as f:
            data = f.read()

        if data:
            print(f'Data received from pipe: "{data}"')

except KeyboardInterrupt:
    print("\nClient stopped.")
