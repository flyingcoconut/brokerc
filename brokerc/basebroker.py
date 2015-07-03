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
import os

class BaseBroker(object):
    def __init__(self, name, drivers):
        self.name = name
        self.drivers = drivers
        self._driver = None

    def list_drivers(self):
        return self.drivers

    def list_metadata(self):
        return self._driver.metadata

    def list_actions(self):
        return self._driver.actions

    def list_options(self):
        self._driver.parser.print_help()

    def list_metadata(self):
        return self._driver.metadata

    def is_loaded(self):
        if self._driver:
            return True
        else:
            return False

    def consume(self, callback):
        self._driver.consume(callback)

    def publish(self, message):
        self._driver.publish(message)

    def load_driver(self, driver_name=None, args=None, callback=None):
        if driver_name in self.list_drivers():
            driver_module = importlib.import_module("." + driver_name, "brokerc.brokers." + self.name)
            driver = getattr(driver_module, 'Driver')
            self._driver = driver(driver_name, args, callback)
        else:
            for driver_name in self.list_drivers():
                driver_module = importlib.import_module("." + driver_name, "brokerc.brokers." + self.name)
                driver = getattr(driver_module, 'Driver')
                self._driver = driver(driver_name, args, callback)

    def parse_arguments(self):
        self._driver.parse_arguments()

    def initialize(self):
        self._driver.initialize()

    def close(self):
        self._driver.close()
