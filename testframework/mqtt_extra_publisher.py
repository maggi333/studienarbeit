__author__ = "Maximilian Rasch"

import paho.mqtt.client as paho
import time


def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))


def on_publish(client, userdata, mid):
    print("mid: " + str(mid))


def on_message(client, userdata, message):

    #payload = bytearray(b'\x00' * 100)
    (rc, mid) = client.publish("mr/info", message.payload, qos=1)

client = paho.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("mr/zustand", qos=1)

client.loop_forever()






