import logging
import asyncio
import time

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


class CoAPClient():
    def __init__(self, packet_size, cycle_time, count, ui):
        self.cycle_time = cycle_time
        self.packet_size = packet_size
        self.count = count
        self.ui = ui

    async def main(self):
        """
        Example class which performs single PUT request to localhost
        port 5683 (official IANA assigned CoAP port), URI "/other/block".
        Request is sent 2 seconds after initialization.
        Payload is bigger than 1kB, and thus is sent as several blocks.
        """

        context = await Context.create_client_context()

        await asyncio.sleep(2)

        # payload = b"The quick brown fox jumps over the lazy dog.\n" * 30
        payload = bytearray(b'\x00' * self.packet_size)
        request = Message(code=PUT, payload=payload)
        request.opt.uri_host = '127.0.0.1'
        request.opt.uri_path = ("other", "block")

        # TODO: mehrere Nachrichten in Schleife verschicken


        for count in range(1, self.count):
            timestamps.append(time.time())
            response = await context.request(request).response
            latenz = time.time() - timestamps.pop(0)
            latency.append(latenz)
            print("Latenz : " + str(latenz) + "s")
            print('Result: %s\n%r' % (response.code, response.payload))
            await asyncio.sleep(self.cycle_time)

    def start_connect(self):
        asyncio.get_event_loop().run_until_complete(self.main())
