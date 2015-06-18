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


class Output(object):
    def __init__(self, stats=False, fields=None):
        self.stats = stats
        self.fields = fields

    def output(self, message):
        out = []
        if self.fields:
            for field in self.fields:
                try:
                    out.append(str(field) + ': ' + str(message[field]))
                except KeyError:
                    pass
        else:
            for field in message:
                out.append(str(field) + ': ' + str(message[field]))
        print(' '.join(out))
        
            
