import paho.mqtt.client as paho
import time
import datetime


def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))


def on_publish(client, userdata, mid):
    latenz = time.time() - timestart
    print("Latenz : " + str(latenz) + "s")
    print("mid: " + str(mid))


testfile = bytearray(b'\x00' * 1024 * 1024 )

client = paho.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.connect("localhost", 1883)

client.loop_start()

while True:
    #timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    #(rc, mid) = client.publish("mr/time", timestamp, 2)
    timestart = time.time()
    (rc, mid) = client.publish("mr/time", testfile, 1)

    time.sleep(5)
