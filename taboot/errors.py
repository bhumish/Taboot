# -*- coding: utf-8 -*-
# Taboot - Client utility for performing deployments with Func.
# Copyright © 2009,2011-2012, Red Hat, Inc.
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


class TabootException(Exception):
    """
    Base Taboot Exception
    """
    pass


class FuncException(TabootException):
    """
    Exception raised whenever a func request returns REMOTE_ERROR
    """

    def __repr__(self):
        """
        Pretty printing
        """
        s = "FuncException:\n"
        s += '\n'.join(self.args[0])
        return s

    def __str__(self):
        return repr(self)


class TabootTaskNotFoundException(TabootException):
    """
    Exception raised if a task can not be found during document
    validation.
    """


class TabootMalformedYAMLException(TabootException):
    pass


class TabootConcurrencyException(TabootException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr("Concurrency Set and Non-concurrent task: %s present"
                    % self.value)
