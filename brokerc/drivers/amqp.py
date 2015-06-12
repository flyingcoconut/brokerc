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

import pika


class AmqpDriver(driver.BaseDriver):
    def __init__(self):
        driver.BaseDriver.__init__(self)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
        channel = connection.channel()
        channel.exchange_declare(exchange='fluentd', type='direct', durable=True)
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange='fluentd', queue=queue_name, routing_key="fluentd-tag")
        def callback(ch, method, properties, body):
            print(" [x] %r:%r" % (method.routing_key, body,))

    def consume(self, callback):
        channel.basic_consume(callback, queue=queue_name, no_ack=True)
        channel.start_consuming()

    def publish(self, message):
        channel.basic_publish(exchange='', routing_key='hello', body=message)



