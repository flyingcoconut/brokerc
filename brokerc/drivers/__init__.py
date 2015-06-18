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

import importlib

__brokers__ = [
    'null',
    'amqp',
    'azure',
    'ironmq',
    'kafka',
    'mqtt',
    'nsq',
    'redis',
    'sqs',
    'stomp',
    'zmq'
]

def list_brokers():
    return __brokers__

def list_drivers(broker):
    if broker not in __brokers__:
        raise ValueError("Broker : " + str(broker) + " : is not valid")
    try:
        broker_module = importlib.import_module("." + broker, "brokerc.drivers")
    except Exception as e:
        raise ImportError("Impossible to load : " + str(broker) + " : " + str(e))
    return broker_module.drivers.keys()

def load(broker, driver, args, callback):
    if broker not in __brokers__:
        raise ValueError("Broker : " + str(broker) + " : is not valid")
    try:
        broker_module = importlib.import_module("." + broker, "brokerc.drivers")
    except Exception as e:
        raise ImportError("Impossible to load : " + str(broker) + " : " + str(e))

    if driver:
        try:
            driver_name = broker_module.drivers[driver]
        except KeyError:
            raise ValueError("Driver : " + str(driver) + " : is not valid")
        try:
            driver_module = importlib.import_module("." + driver, "brokerc.drivers." + broker)
            driver = getattr(driver_module, driver_name)
        except Exception as e:
            raise ImportError("Impossible to load : " + str(driver) + " : " + str(e))
        return driver(args, callback)

    else:
        for driver in broker_module.drivers.keys():
            driver_name = broker_module.drivers[driver]
            driver_module = importlib.import_module("." + driver, "brokerc.drivers." + broker)
            driver = getattr(driver_module, driver_name)
            return driver(args, callback)
