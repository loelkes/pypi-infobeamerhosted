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

import requests
import os
import json
import logging

from Exceptions import *

logger = logging.getLogger(__name__)

class InfobeamerAPI:
    def __init__(self, key=False, user=False, url=False):
        self.user = user or InfobeamerAPI.USER
        self.key = key or InfobeamerAPI.KEY
        self.url = url or InfobeamerAPI.URL

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
        if method not in ['GET', 'POST', 'DELETE']:
            raise APIError()
        if method is 'GET':
            result = requests.get(f'{self.url}{endpoint}', auth=self.auth, params=payload)
        elif method is 'POST':
            result = requests.post(f'{self.url}{endpoint}', auth=self.auth, data=payload)
        elif method is 'DELETE':
            result = requests.delete(f'{self.url}{endpoint}', auth=self.auth, data=payload)
        if result.status_code == requests.codes.ok:
            self.status = True
            self.response = result.json()
        elif result.status_code == 400:
            self.error = result.json()
            self.response = None
        return self.status
