from API import *
from threading import Thread
from queue import Queue
from API import InfobeamerAPI as API

import logging
logger = logging.getLogger(__name__)

class Infobeamer(API):
    def __init__(self, key=False):
        super().__init__(key)
        self.setups = Setups(key)
        self.devices = []
        self.group = ''

    @property
    def group(self):
        try:
            return self.__group
        except: # AttributeError
            return ''

    @group.setter
    def group(self, value):
        self.__group = value

    def getSetup(self, serial=0, id=0):
        for setup in self.setups:
            if setup.id == int(id):
                return setup
            else:
                continue
        return False

class Setups(API):
    def __init__(self, key):
        super().__init__(key)
        self.groups = []
        self.group = ''
        self.getSetups()

    @property
    def group(self):
        try:
            return self.__groupname
        except: # AttributeError
            return ''

    @group.setter
    def group(self, name):
        self.__groupname = name

    @property
    def all(self):
        return self.__setups;

    @all.setter
    def all(self, value):
        self.__setups = value

    @property
    def selection(self):
        return [setup for setup in self.all if setup.inGroup(self.group)]

    def getSetups(self):
        if not self.query('setup/list'):
            raise APIError()
        self.all = [Setup(setup) for setup in self.response['setups']]
        logger.info(f'Found a total of {len(self.all)} Setups.')
        for setup in self.all:
            if setup.group and setup.group not in self.groups:
                self.groups.append(setup.group)
        logger.info(f'Found the following groups {self.groups}')

class Setup:
    def __init__(self, config):
        self.__dict__.update(config)

    def inGroup(self, groupname):
        if groupname == self.group:
            return True
        else:
            return False

    @property
    def group(self) -> str:
        return self.userdata.get('group',False)
