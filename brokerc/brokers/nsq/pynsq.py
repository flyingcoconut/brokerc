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
    import nsq
except ImportError:
    raise ImportError("package pynsq is not installed")


class PynsqDriver(driver.BaseDriver):
    def __init__(self, args, callback):
        driver.BaseDriver.__init__(self, args, callback)

    def create_message(self, message):
        msg = message.Message()
        
    def consume(self, callback):
        reader = nsq.Reader(message_handler=self.create_message, 
                 lookupd_http_addresses=['http://127.0.0.1:4161'],
                 topic=self.args.topic,
                 channel=self.args.channel,
                 lookupd_poll_interval=5
        )
        nsq.run()

    def publish(self, message):
        pass

    def close(self):
        pass



