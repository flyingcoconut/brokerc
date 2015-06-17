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

from brokerc.drivers import driver
import redis


class RedispyDriver(driver.BaseDriver):
    def __init__(self, args, callback):
        driver.BaseDriver.__init__(self, args, callback)

    def initialize(self):
        self.connection = redis.StrictRedis(host=self.args.host, port=self.args.port)
        self.pubsub = self.connection.pubsub(ignore_subscribe_messages=True)
        
    def consume(self, callback):
        self.pubsub.subscribe(self.args.channel)
        while True:
            message = self.pubsub.get_message()
            if message:
                    self.callback(message)
            time.sleep(0.0001)

    def publish(self, message):
        for channel in self.args.channel:
            self.connection.publish(channel, message)

    def close(self):
        pass



