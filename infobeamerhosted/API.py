import requests
import os
import json
import logging

from Exceptions import *

logger = logging.getLogger(__name__)

class InfobeamerAPI:
    def __init__(self, key=False, user=False, url=False):
        self.user = user
        self.key = key
        self.url = url
        self.task_num = 5

    def setupRequests(self):
        self.status = False
        self.response = None
        self.error = None

    @property
    def key(self) -> str:
        return self.__api_key or ''

    @key.setter
    def key(self, value: str):
        if not value:
            raise MissingAPIKeyError()
        self.__api_key = value

    @property
    def user(self) -> str:
        return self.__api_user or ''

    @user.setter
    def user(self, value: str):
        self.__api_user = value

    @property
    def url(self) -> str:
        return self.__api_url or 'https://info-beamer.com/api/v1/'

    @url.setter
    def url(self, value: str):
        self.__api_url = value

    @property
    def auth(self):
        pass

    @auth.getter
    def auth(self):
        return requests.auth.HTTPBasicAuth(self.user, self.key)

    def query(self, endpoint='ping', method='GET', payload={}):
        result = None
        self.status = False
        if method is 'GET':
            result = requests.get(f'{self.url}{endpoint}',
                auth=self.auth, params=payload)
        elif method is 'POST':
            result = requests.post(f'{self.url}{endpoint}',
                auth=self.auth, data=payload)
        elif method is 'DELETE':
            result = requests.delete(f'{self.url}{endpoint}',
                auth=self.auth, data=payload)
        if result.status_code == requests.codes.ok:
            self.status = True
            self.response = result.json()
        elif result.status_code == 400:
            self.error = result.json()
            self.response = None
        return self.status
