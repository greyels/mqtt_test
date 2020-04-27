from paho.mqtt import client
import json
import random


def main():
    # Publish order
    path = "mqtt/pos"
    order = {"id": 1, "items": [{'pizza': 1, 'pasta': 2, 'cola': 2}], "locked": False}
    publisher = client.Client()
    publisher.connect("127.0.0.1", bind_port=random.randint(49152, 65535))
    print(f"Client TCP port: {publisher._bind_port}")
    print(f"Publishing {order} to {path}")
    publisher.publish(topic=path, qos=1, payload=json.dumps(order))


if __name__ == "__main__":
    main()
