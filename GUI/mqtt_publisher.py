import paho.mqtt.client as paho
import time
import datetime

timestamps = []
latency = []


def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))


def on_publish(client, userdata, mid):
    latenz = time.time() - timestamps.pop(0)
    latency.append(latenz)
    print("Latenz : " + str(latenz) + "s")
    print("mid: " + str(mid))


class Publisher():
    def calc_latency(self):
        sum = 0
        i = 0
        for item in latency:
            sum = sum + item
            i += 1
        return sum / i

    def start_connect(self):
        testfile = bytearray(b'\x00' * 1024 * 1024)

        client = paho.Client()
        client.on_connect = on_connect
        client.on_publish = on_publish
        client.connect("localhost", 1883)

        client.loop_start()

        for counter in range(1, 5):
            # timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            # (rc, mid) = client.publish("mr/time", timestamp, 2)
            timestamps.append(time.time())
            (rc, mid) = client.publish("mr/time", testfile, 1)

            time.sleep(0.5)
