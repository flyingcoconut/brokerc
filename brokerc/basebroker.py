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

class DriverNotLoadedError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class LoadDriverError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

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

    def list_dependencies(self):
        return self._driver.dependencies.keys()

    def list_actions(self):
        return self._driver.actions

    def is_loaded(self):
        if self._driver:
            return True
        else:
            return False

    def consume(self, callback):
        self._driver.consume(callback)

    def publish(self, message):
        self._driver.publish(message)

    def test(self, driver_name=None):
        report = {}
        if driver_name:
            report[driver_name] = self._test(driver_name)
        else:
            for driver_name in self.drivers:
                report[driver_name] = self._test(driver_name)
        return report

    def _test(self, driver_name):
        report = {}
        try:
            self.load_driver(driver_name)
            self.import_dependencies()
        except Exception as e:
            report['status'] = 'Fail'
            report['error'] = str(e)
        else:
            report['status'] = 'Succeed'
            report['error'] = 'None'
        return report

    def load_driver(self, driver_name=None, args=None, callback=None):
        if driver_name:
            self._load_driver(driver_name, args, callback)
        else:
            for driver_name in self.list_drivers():
                self._load_driver(driver_name, args, callback)

    def _load_driver(self, driver_name, args, callback):
        driver_module = importlib.import_module("." + driver_name, "brokerc.brokers." + self.name)
        driver = getattr(driver_module, 'Driver')
        try:
            self._driver = driver(driver_name, args, callback)
        except Exception as e:
            raise LoadDriverError(e)
                
    def parse_arguments(self):
        self._driver.parse_arguments()

    def import_dependencies(self):
        self._driver.import_dependencies()

    def initialize(self):
        self._driver.initialize()

    def close(self):
        self._driver.close()
