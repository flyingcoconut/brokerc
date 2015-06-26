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

from brokerc import basebroker
import argparse

parser = argparse.ArgumentParser(description='Redis Broker')
parser.add_argument('--host', metavar='HOSTNAME', type=str, default="localhost", help='redis hostname')
parser.add_argument('--port', metavar='PORT', type=int, default=6379, help='redis port')
parser.add_argument('--channel', metavar='N', type=str, nargs='+', required=True, help='channel name')
parser.add_argument('--pattern', metavar='N', type=str, nargs='+', help='subscription pattern')



