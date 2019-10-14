import requests
import os
import json
import logging
logger = logging.getLogger(__name__)

class Infobeamer:
    def __init__(self, url, user, key):
        self.user = user
        self.key = key
        self.url = url
        self.setupRequests()
        self.task_num = 5

    def setupRequests(self):
        self.__auth = requests.auth.HTTPBasicAuth(self.user, self.key)
        self.status = False
        self.response = None
        self.error = None

    @property
    def key(self) -> str:
        return self.__api_key

    @key.setter
    def key(self, value: str):
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

    def query(self, endpoint='ping', method='GET', payload={}):
        result = None
        self.status = False
        if method is 'GET':
            result = requests.get(f'{self.url}{endpoint}',
                auth=self.__auth, params=payload)
        elif method is 'POST':
            result = requests.post(f'{self.url}{endpoint}',
                auth=self.__auth, data=payload)
        elif method is 'DELETE':
            result = requests.delete(f'{self.url}{endpoint}',
                auth=self.__auth, data=payload)
        if result.status_code == requests.codes.ok:
            self.status = True
            self.response = result.json()
        elif result.status_code == 400:
            self.error = result.json()
            self.response = None
        return self.status
