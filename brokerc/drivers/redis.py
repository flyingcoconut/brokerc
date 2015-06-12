#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Patrick Charron
# Email : patrick.charron.pc@gmail.com
# Description : Broker Client
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

from brokerc.drivers import driver

import redis


class RedisDriver(driver.BaseDriver):
    def __init__(self, args):
        driver.BaseDriver.__init__(self, args)
        self.connection = redis.StrictRedis(host=self.args.host, port=self.args.port)
        self.pubsub = self.connection.pubsub()
        
    def consume(self, callback):
        self.pubsub.subscribe("test")
        print(self.pubsub.get_message())

    def publish(self, message):
        self.connection.publish("test", "allobonjour")



