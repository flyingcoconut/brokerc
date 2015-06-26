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

from brokerc import driver
from brokerc import message

import pika

class PikaDriver(driver.BaseDriver):
    def __init__(self, args, callback):
        driver.BaseDriver.__init__(self, args, callback)

    def initialize(self):
        pika.ConnectionParameters(host=self.args.host)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.args.host))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.args.exchange, type='direct', durable=True)
        self.result = self.channel.queue_declare(exclusive=True)
        self.queue_name = self.result.method.queue
        self.channel.queue_bind(exchange=self.args.exchange, queue=self.queue_name, routing_key=self.args.key)
        def callback(ch, method, properties, body):
            print(" [x] %r:%r" % (method.routing_key, body,))

    def create_message(self, ch, method, properties, body):
        msg = message.Message()
        msg.body = body.decode("utf-8")
        msg.metadata['method'] = method
        msg.metadata['consumer_tag'] = method.consumer_tag
        msg.metadata['delivery_tag'] = method.delivery_tag
        msg.metadata['redelivered'] = method.redelivered
        msg.metadata['exchange'] = method.exchange
        msg.metadata['key'] = method.routing_key
        msg.metadata['app_id'] = properties.app_id
        msg.metadata['content_type'] = properties.content_type
        msg.metadata['headers'] = properties.headers
        self.callback(msg)

    def consume(self, callback):
        self.channel.basic_consume(self.create_message, queue=self.queue_name, no_ack=True)
        self.channel.start_consuming()

    def publish(self, message):
        self.channel.basic_publish(exchange=self.args.exchange, routing_key=self.args.key, body=message)

    def close(self):
        self.connection.close()



