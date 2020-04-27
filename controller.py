from paho.mqtt import client, publish
import json
import random
import time


def on_connect(client, userdata, flags, rc):
    path = "mqtt/pos"
    print("Connected with result code: %s" % rc)
    client.subscribe(path, qos=1)
    print(f"Client TCP port: {client._bind_port}")
    print(f"Subscribed to {path}")

def on_message(client, userdata, msg):
    order = json.loads(msg.payload.decode('utf-8'))
    print()
    print(f"Received {order} on {msg.topic}")
    print("Processing the order...")
    # Make manipulations with order and store to the DB
    order['locked'] = True
    order['updated_on'] = time.ctime()
    # Publish order back to pos stations
    path = "mqtt/controller"
    print(f"Publishing {order} to {path}")
    publish.single(topic=path, payload=json.dumps(order), qos=1)


def main():
    # Subscribe to pos
    subscriber = client.Client(client_id='controller', clean_session=False)
    subscriber.on_connect = on_connect
    subscriber.on_message = on_message
    subscriber.connect("127.0.0.1", bind_port=random.randint(49152, 65535))
    subscriber.loop_forever()


if __name__ == "__main__":
    main()
