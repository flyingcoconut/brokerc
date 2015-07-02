#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Patrick Charron
# Email : patrick.charron.pc@gmail.com
# Description : Message Broker Client
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time

from brokerc import driver
from brokerc import message

try:
    import redis
except ImportError:
    raise ImportError("package redis is not installed")


class Driver(driver.BaseDriver):
    def __init__(self, description, args, callback):
        driver.BaseDriver.__init__(self, description, args, callback)
        self.actions = ['consume', 'publish', 'list-channels', 'list-subscribers']
        self.parser.add_argument('--host', metavar='HOSTNAME', type=str, default="localhost", help='redis hostname')
        self.parser.add_argument('--port', metavar='PORT', type=int, default=6379, help='redis port')
        self.parser.add_argument('--channel', metavar='N', type=str, nargs='+', required=True, help='channel name')
        self.parser.add_argument('--pattern', metavar='N', type=str, nargs='+', help='subscription pattern')

    def initialize(self):
        self.connection = redis.StrictRedis(host=self.args.host, port=self.args.port)
        self.pubsub = self.connection.pubsub(ignore_subscribe_messages=True)
        
    def consume(self, callback):
        self.pubsub.subscribe(self.args.channel)
        while True:
            data = self.pubsub.get_message()
            if data:
                msg = message.Message()
                msg.body = data['data'].decode("utf-8")
                msg.metadata['channel'] = data['channel'].decode("utf-8")
                #msg.metadata['pattern'] = data['pattern'].decode("utf-8")
                msg.metadata['type'] = data['type']
                self.callback(msg)
            time.sleep(0.0001)

    def publish(self, message):
        for channel in self.args.channel:
            self.connection.publish(channel, message)

    def close(self):
        pass



