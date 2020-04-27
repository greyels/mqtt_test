from paho.mqtt import client
import random
import json


def on_connect(client, userdata, flags, rc):
    path = "mqtt/controller"
    print("Connected with result code: %s" % rc)
    client.subscribe(path, qos=1)
    print(f"Client TCP port: {client._bind_port}")
    print(f"Subscribed to {path}")

def on_message(client, userdata, msg):
    order = json.loads(msg.payload.decode('utf-8'))
    print()
    print(f"Received {order} on {msg.topic}")


def main():
    # Subscribe to controller
    subscriber = client.Client(client_id='1', clean_session=False)
    subscriber.on_connect = on_connect
    subscriber.on_message = on_message
    subscriber.connect("127.0.0.1", bind_port=random.randint(49152, 65535))
    subscriber.loop_forever()


if __name__ == "__main__":
    main()
