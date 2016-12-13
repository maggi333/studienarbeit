import paho.mqtt.client as paho
import time

timestamps = []
latency = []
msg_send = []
msg_ack = []


# msg_sub = []


def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))


def on_publish(client, userdata, mid):
    msg_ack.append((mid, time.time()))
    latenz = time.time() - timestamps.pop(0)
    latency.append(latenz)
    print("Latenz : " + str(latenz) + "s")
    print("mid: " + str(mid))


def on_message(client, userdata, message):
    msg_ack.append((message.payload[-1], time.time()))
    latenz = time.time() - timestamps.pop(0)
    latency.append(latenz)
    print("Latenz : " + str(latenz) + "s")
    print("mid: " + str(message.payload[-1]))


class MQTTPublisher():
    def __init__(self, packet_size, cycle_time, count, qos, extra_client, ui):
        self.cycle_time = cycle_time
        self.testfile = bytearray(b'\x00' * packet_size)
        self.count = count
        self.QoS = qos
        self.extra = extra_client
        self.ui = ui

    def start_connect(self):
        # Löschen der Zwischenspeicherlisten
        latency.clear()
        timestamps.clear()
        msg_send.clear()
        msg_ack.clear()
        # msg_sub.clear()

        client = paho.Client()
        client.on_connect = on_connect
        # client.on_publish = on_publish
        # client.on_message = on_message
        client.connect("localhost", 1883)

        client.loop_start()
        # start_time = time.time()

        # Mit Extra Client?
        if self.extra:

            client.on_message = on_message

            # TODO Ressource vorher löschen
            client.subscribe("mr/info", self.QoS)
            for counter in range(0, self.count):

                self.testfile[-1] = counter     # setze Makierung
                send_time = time.time()
                timestamps.append(send_time)
                (rc, mid) = client.publish("mr/zustand", self.testfile, self.QoS)
                msg_send.append((counter, send_time))
                self.ui.progressBar.setValue((counter / self.count) * 100)
                time.sleep(self.cycle_time)

            return msg_send, msg_ack


        elif not self.extra:

            client.on_publish = on_publish

            for counter in range(0, self.count):
                # timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                # (rc, mid) = client.publish("mr/time", timestamp, 2)
                send_time = time.time()
                timestamps.append(send_time)
                (rc, mid) = client.publish("mr/time", self.testfile, self.QoS)
                msg_send.append((mid, send_time))
                self.ui.progressBar.setValue((counter / self.count) * 100)
                time.sleep(self.cycle_time)

            # print(time.time()-start_time)
            # WICHTIG: lange genug warten damit jede Nachricht angekommen ist
            if len(timestamps) > 0:
                print('Warte 5s')
                time.sleep(5)
            return msg_send, msg_ack
