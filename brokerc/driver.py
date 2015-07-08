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

class DependenciesError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class BaseDriver(object):
    def __init__(self, description, args, callback):
        self.args = args
        self.callback = callback
        self.actions =  []
        self.metadata = {}
        self.dependencies = []
        self.parser = argparse.ArgumentParser(prog='Driver(' + description + ')', usage='--driver ' + description + ' [OPTIONS]')


    def parse_arguments(self):
        self.args = self.parser.parse_args(self.args)

    def initialize(self):
        pass

    def publish(self, message):
        pass

    def consume(self, callback):
        pass

    def close(self):
        pass
