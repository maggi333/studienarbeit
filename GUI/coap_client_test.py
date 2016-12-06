import logging
import asyncio
import time
import math_func
import threading
from aiocoap import *

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


class CoAPClient():
    def __init__(self, packet_size, cycle_time, count, ui):
        self.cycle_time = cycle_time
        self.packet_size = packet_size
        self.count = count
        self.ui = ui
        self.payload = bytearray(b'\x00' * self.packet_size)

    async def main(self):
        """
        Example class which performs single PUT request to localhost
        port 5683 (official IANA assigned CoAP port), URI "/other/block".
        Request is sent 2 seconds after initialization.
        Payload is bigger than 1kB, and thus is sent as several blocks.
        """

        context = await Context.create_client_context()

        await asyncio.sleep(0.5)

        request = Message(code=PUT, payload=self.payload)
        request.opt.uri_host = '127.0.0.1'
        request.opt.uri_path = ("other", "block")
        timestamps.append(time.time())
        response = await context.request(request).response
        latenz = time.time() - timestamps.pop(0)
        latency.append(latenz)
        print("Latenz : " + str(latenz) + "s")
        print('Result: %s\n%r' % (response.code, response.payload))

    def start(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.get_event_loop().run_until_complete(self.main())

    def start_connect(self):
        # Löschen der Zwischenspeicherlisten
        latency.clear()
        timestamps.clear()

        start_time = time.time()
        for i in range(0, self.count):
            t = threading.Thread(target=self.start)
            threads.append(t)
            t.start()
            time.sleep(self.cycle_time)
            self.ui.progressBar.setValue((i / self.count) * 100)
        print(time.time() - start_time)

        if len(threads) > 0:
            print('Warte 5s')
            time.sleep(5)
            if len(threads) >0:
                print('Warte 5s')
                time.sleep(5)

    def evaluation(self):
        return math_func.calc_latency(latency)