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

import zmq

class ZmqDriver(object):
    def __init__(self, args):
        self.args = args

    def initialize(self):
        pass

    def publish(self, message):
        ctx = zmq.Context()
        socket = ctx.socket(zmq.PUB)
        socket.bind('tcp://127.0.0.1:4999')
        socket.send_string(message)


    def consume(self, callback):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.setsockopt_string(zmq.SUBSCRIBE, '')
        socket.connect('tcp://127.0.0.1:4999')
        while True:
            msg = socket.recv_string()
            print(msg)

    def close(self):
        pass
