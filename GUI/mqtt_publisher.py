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
    def __init__(self, packet_size, cycle_time, count, QoS, ui):
        self.cycle_time = cycle_time
        self.packet_size = packet_size
        self.count = count
        self.QoS = QoS
        self.ui = ui


    def calc_latency(self):
        sum = 0
        i = 0
        for item in latency:
            sum = sum + item
            i += 1
        return round(sum / i, 3)

    def start_connect(self):
        testfile = bytearray(b'\x00' * self.packet_size)

        client = paho.Client()
        client.on_connect = on_connect
        client.on_publish = on_publish
        client.connect("localhost", 1883)

        client.loop_start()

        for counter in range(1, self.count):
            # timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            # (rc, mid) = client.publish("mr/time", timestamp, 2)
            timestamps.append(time.time())
            (rc, mid) = client.publish("mr/time", testfile, self.QoS)

            time.sleep(self.cycle_time)
            self.ui.progressBar.setValue((counter/self.count)*100)
