import paho.mqtt.client as paho
import time
import datetime


def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))


def on_publish(client, userdata, mid):
    print("mid: " + str(mid))


client = paho.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.connect("broker.hivemq.com", 1883)

client.loop_start()

while True:
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    (rc, mid) = client.publish("mr/time", timestamp, 2)
    time.sleep(5)
