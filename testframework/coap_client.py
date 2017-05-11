__author__ = "Maximilian Rasch"

import logging
import asyncio
import time
import threading
from aiocoap import *
# TODO Framework unabhaenging vom Surfstick machen
import huaweiE3372

# This file is part of the Python aiocoap library project.
#
# Copyright (c) 2012-2014 Maciej Wasilak <http://sixpinetrees.blogspot.com/>,
#               2013-2014 Christian Amsüss <c.amsuess@energyharvesting.at>
#
# aiocoap is free software, this file is published under the MIT license as
# described in the accompanying LICENSE file.


logging.basicConfig(level=logging.INFO)

timestamps = []
latency = []
threads = []
msg_send = []
msg_ack = []


class CoAPClient():
    def __init__(self, packet_size, cycle_time, count, ui, getsignal):
        self.cycle_time = cycle_time
        self.count = count
        self.ui = ui
        self.payload = bytearray(b'\x00' * packet_size)
        self.getsignal = getsignal

    async def main(self):
        """
        Example class which performs single PUT request to localhost
        port 5683 (official IANA assigned CoAP port), URI "/other/block".
        Request is sent 2 seconds after initialization.
        Payload is bigger than 1kB, and thus is sent as several blocks.
        """

        context = await Context.create_client_context()

        # await asyncio.sleep(0.5)

        request = Message(code=PUT, payload=self.payload)
        request.opt.uri_host = 'localhost'  # hier IP Adresse vom Server eintragen
        request.opt.uri_path = ("other", "block")
        if self.getsignal:
            rsrq, rsrp, rssi, sinr = huaweiE3372.signal()  # frage Signalstaerke ab
        else:
            rsrq, rsrp, rssi, sinr = 0, 0, 0, 0
        send_time = time.time()
        timestamps.append(send_time)
        msg_send.append((context.message_id, send_time,rsrq, rsrp, rssi, sinr))
        response = await context.request(request).response
        ack_time = time.time()
        try:
            msg_ack.append((response.mid - response.opt.block1[0] * 2, ack_time)) # TODO: Erklärung
        except TypeError:
            msg_ack.append((response.mid, ack_time))
        latenz = time.time() - timestamps.pop(0)
        latency.append(latenz)
        print("Latenz : " + str(latenz) + "s")
        #print('Result: %s\n%r' % (response.code, response.payload))

    def start(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.get_event_loop().run_until_complete(self.main())

    def start_connect(self):
        # Löschen der Zwischenspeicherlisten
        latency.clear()
        timestamps.clear()
        msg_send.clear()
        msg_ack.clear()

        # start_time = time.time()
        for i in range(0, self.count):
            t = threading.Thread(target=self.start)
            threads.append(t)
            t.start()
            self.ui.progressBar.setValue((i / self.count) * 100)
            time.sleep(self.cycle_time)

        # print(time.time() - start_time)

        if len(timestamps) > 0:
            print('Warte 5s', len(timestamps))
            time.sleep(5)
            if len(timestamps) > 0:
                print('Warte 5s', len(timestamps))
                time.sleep(5)
        return msg_send, msg_ack
