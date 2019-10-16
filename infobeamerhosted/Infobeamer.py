# Copyright 2019 Christian Lölkes

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from threading import Thread
from queue import Queue
from infobeamerhosted.API import InfobeamerAPI

import logging
logger = logging.getLogger(__name__)

class Infobeamer(InfobeamerAPI):
    def __init__(self):
        super().__init__()
        self.setups = Setups()
        self.devices = Devices()
        self.packages = Packages()
        self.assets = Assets()
        self.group = ''

    @property
    def group(self) -> str:
        try:
            return self.__group
        except: # AttributeError
            return ''

    @group.setter
    def group(self, name: str):
        self.__group = name
        self.devices.group = name
        self.setups.group = name
        self.packages.group = name
        self.assets.group = name

class GroupBase(InfobeamerAPI):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self.getItems()

    @property
    def group(self) -> str:
        try:
            return self.__groupname
        except: # AttributeError
            return ''

    @group.setter
    def group(self, name: str):
        self.__groupname = name

    @property
    def all(self) -> list:
        return self.__items;

    @all.setter
    def all(self, items: list):
        self.__items = items

    @property
    def selection(self) -> list:
        if self.group:
            return [item for item in self.all if item.inGroup(self.group)]
        else:
            return self.all

    def getItems(self):
        if not self.query(f'{self.target.NAME}/list'):
            raise APIError()
        self.all = [self.target(item) for item in self.response[self.target.NAME + 's']]
        logger.info(f'Found a total of {len(self.all)} {self.target.NAME}s.')

class Setups(GroupBase):
    def __init__(self):
        super().__init__(Setup)

class Devices(GroupBase):
    def __init__(self):
        super().__init__(Device)

class Assets(GroupBase):
    def __init__(self):
        super().__init__(Asset)

class Packages(GroupBase):
    def __init__(self):
        super().__init__(Package)


class ItemBase(InfobeamerAPI):
    def __init__(self, target):
        self.target = target
        self.payload = {}

    def inGroup(self, groupname: str) -> bool:
        if groupname == self.group:
            return True
        else:
            return False

    def update(self, option=None, payload=False) -> bool:
        if self.query(f'{self.target}/{self.id}/{option}', 'POST', payload or self.payload) and self.response.ok:
            logger.info(f'Updated {self.target} with id={self.id}')
            return True
        logger.error(f'Could not update {self.target} with id={self.id}')
        return False

    def delete(self) -> bool:
        if self.query(f'{self.target}/{self.id}/', 'DELETE') and self.response.ok:
            logger.info(f'Deleted {self.target} with id={self.id}')
            return True
        logger.error(f'Could not delete {self.target} with id={self.id}')
        return False

    @property
    def group(self) -> str:
        return self.userdata.get('group','')

    @group.setter
    def group(self, name: str):
        self.userdata.update({'group': name})
        self.update(payload=self.userdata)

class Device(ItemBase):
    NAME = 'device'
    def __init__(self, config):
        super().__init__('device')
        self.__dict__.update(config)

    def assignSetup(self, id=0):
        self.update({'setup_id': id})

    def reboot(self):
        self.query('reboot')

class Setup(ItemBase):
    NAME = 'setup'
    def __init__(self, config):
        super().__init__('setup')
        self.__dict__.update(config)

class Asset(ItemBase):
    NAME = 'asset'
    def __init__(self, config):
        super().__init__('asset')
        self.__dict__.update(config)

class Package(ItemBase):
    NAME = 'package'
    def __init__(self, config):
        super().__init__('package')
        self.__dict__.update(config)
