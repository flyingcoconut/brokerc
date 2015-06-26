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
    def __init__(self, stats=False, metadata=None):
        self.stats = stats
        self.metadata = metadata

    def output(self, message):
        out = []
        if self.metadata:
            for data in self.metadata:
                try:
                    out.append(str(data) + ': ' + str(message.metadata[data]))
                except KeyError:
                    pass
            out.append('message: ' + message.body)
        else:
            out.append(message.body)
        print(', '.join(out))
        
            

