# -*- coding: utf-8 -*-
# Taboot - Client utility for performing deployments with Func.
# Copyright © 2009,2011, Red Hat, Inc.
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

from taboot.tasks import command


class ServiceBase(command.Run):
    """
    Base Class for system service tasks
    """
    pass


class Start(ServiceBase):
    """
    Start a service.

    Arguments:
      - ``service`` - The service to start.
    """

    def __init__(self, service, **kwargs):
        super(Start, self).__init__('service %s start' % service, **kwargs)


class Stop(ServiceBase):
    """
    Stop a service.

    Arguments:
      - ``service`` - The service to stop.
    """

    def __init__(self, service, **kwargs):
        super(Stop, self).__init__('service %s stop' % service, **kwargs)


class Restart(ServiceBase):
    """
    Restart a service.

    Arguments:
      - ``service`` - The service to restart.
    """

    def __init__(self, service, **kwargs):
        super(Restart, self).__init__('service %s restart' % service, **kwargs)


class Graceful(ServiceBase):
    """
    Gracefully restart a service.

    Arguments:
      - ``service`` - The service to gracefully restart.
    """

    def __init__(self, service, **kwargs):
        super(Graceful, self).__init__('service %s graceful' % service, **kwargs)
