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

from kafka import SimpleProducer, KafkaClient
from kafka import KafkaConsumer
from kafka.common import LeaderNotAvailableError


class KafkaDriver(object):
    def __init__(self, args):
        self.args = args

    def initialize(self):
        pass

    def publish(self, message):
        kafka = KafkaClient("192.168.33.10:9092")
        producer = SimpleProducer(kafka)
     
        topic = b'test'
        msg = b'Hello World'
     
        try:
            print_response(producer.send_messages(topic, msg))
        except LeaderNotAvailableError:
            time.sleep(1)
            print_response(producer.send_messages(topic, msg))
     
        kafka.close()

    def consume(self, callback):
        consumer = KafkaConsumer(b"test", group_id=b"my_group_id", metadata_broker_list=["192.168.33.10:9092"])
        for message in consumer:
            # This will wait and print messages as they become available
            print(message)

    def close(self):
        pass
