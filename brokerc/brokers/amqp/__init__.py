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

import argparse

drivers = {
    'pika': 'PikaDriver'
}

metadata = [
    'channel',
    'type',
    'pattern'
]

parser = argparse.ArgumentParser(prog='amqp', description='AMQP Broker')
parser.add_argument('--host', metavar='HOSTNAME', type=str, default="localhost", help='AMQP hostname')
parser.add_argument('--port', metavar='PORT', type=int, default=5672, help='AMQP port')
parser.add_argument('--prefetch', metavar='QUANTITY', type=int, help='prefetch')
parser.add_argument('--exchange', metavar='EXCHANGE', type=str, required=True, help='exchange name')
parser.add_argument('--vhost', metavar='N', type=str, help='vhost')
parser.add_argument('--queue', metavar='N', type=str, nargs='+', help='queue name')
parser.add_argument('--type', metavar='N', type=str, choices=['direct', 'fanout', 'topic'], help='exchange type')
parser.add_argument('--key', type=str, help='key name')
parser.add_argument('--durable', action='store_true', help='durable exchange')
parser.add_argument('--persistent', action='store_true', help='persistant message')
parser.add_argument('--declare', metavar='N', type=bool, help='declare exchange')
parser.add_argument('--ack', action='store_true', help='ack message')
parser.add_argument('--exclusive', action='store_true', help='exclusive queue')

