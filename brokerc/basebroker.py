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

import logging
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
    def __init__(self, name, drivers, debug_level=logging.NOTSET):
        self.name = name
        self.drivers = drivers
        self._driver = None
        self.debug_level = logging.DEBUG
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - ' + self.name + ' - %(levelname)s - %(message)s')
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def list_drivers(self):
        self.logger.info("Listing drivers")
        self.logger.debug('Available drivers : ' + str(self.drivers))
        return self.drivers

    def list_metadata(self):
        self.logger.info("Listing metada")
        self.logger.debug('Available metadata : ' + str(self._driver.metadata))
        return self._driver.metadata

    def list_actions(self):
        self.logger.info("Listing actions")
        return self._driver.actions

    def list_options(self):
        self.logger.info("Listing options")
        self._driver.parser.print_help()

    def list_dependencies(self):
        self.logger.info("Listing dependencies")
        return self._driver.dependencies.keys()

    def is_loaded(self):
        self.logger.info("Verifying if driver is loaded")
        if self._driver:
            self.logger.info("Driver is loaded")
            return True
        else:
            self.logger.info("Driver is not loaded")
            return False

    def consume(self, callback):
        self.logger.info("Start consuming")
        try:
            self._driver.consume(callback)
        except:
            self.logger.error("Error consuming")
        else:
            self.logger.info("Stop consuming")

    def publish(self, message):
        self.logger.info("Publishing")
        try:
            self._driver.publish(message)
        except:
            self.logger.error("Error publishing")
        else:
            self.logger.info("Message published")

    def test(self, driver_name=None):
        self.logger.info("Sarting driver testing")
        report = {}
        if driver_name:
            report[driver_name] = self._test(driver_name)
        else:
            for driver_name in self.drivers:
                report[driver_name] = self._test(driver_name)
        return report

    def _test(self, driver_name):
        self.logger.info("Testing driver : " + str(driver_name))
        report = {}
        try:
            self.load_driver(driver_name)
            self.import_dependencies()
        except Exception as e:
            self.logger.error("Driver : " + str(driver_name) + ' failed')
            report['status'] = 'Fail'
            report['error'] = str(e)
        else:
            self.logger.info("Driver : " + str(driver_name) + ' succeed')
            report['status'] = 'Succeed'
            report['error'] = 'None'
        return report

    def load_driver(self, driver_name=None, args=None, callback=None):
        if driver_name:
            self.logger.info("Loading driver : " + driver_name)
            self._load_driver(driver_name, args, callback)
        else:
            self.logger.info("Trying to load available drivers")
            for driver_name in self.list_drivers():
                self.logger.info("Loading driver : " + driver_name)
                self._load_driver(driver_name, args, callback)

    def _load_driver(self, driver_name, args, callback):
        self.logger.info("Loading driver module")
        driver_module = importlib.import_module("." + driver_name, "brokerc.brokers." + self.name)
        self.logger.info("Create driver object")
        driver = getattr(driver_module, 'Driver')
        try:
            self._driver = driver(driver_name, args, callback)
        except Exception as e:
            self.logger.error("Impossible to load driver")
            raise LoadDriverError(e)
        else:
            self.logger.info("Driver load successfully")
                
    def parse_arguments(self):
        self.logger.info("Parsing arguments")
        self.logger.debug('Arguments : ' + str(self._driver.args))
        try:
            self._driver.parse_arguments()
        except:
            self.logger.error("Error parsing arguments")
        else:
            self.logger.info("Arguments parsed")

    def import_dependencies(self):
        self.logger.info("Importing dependencies")
        try:
            self._driver.import_dependencies()
        except:
            self.logger("Error importing dependencies")
        else:
            self.logger.info("Dependencies imported")

    def initialize(self):
        self.logger.info("Initializing driver")
        try:
            self._driver.initialize()
        except:
            self.logger.error("Error initializing driver")
        else:
            self.logger.info("Driver initialized")

    def close(self):
        self.logger.info("Closing connection")
        try:
            self._driver.close()
        except:
             self.logger.error("Error closing connection")
        else:
             self.logger.info("Connection closed")
