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

import argparse
import os
import logging

from infobeamerhosted.API import *
from infobeamerhosted.Infobeamer import *

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.info('Script is executed as standalone file.')

# Parse arguments for CLI use.
parser = argparse.ArgumentParser()
parser.add_argument('--api-key', type=str, help='API Key.')
parser.add_argument('--api-user', type=str, default='', help='API User.')
parser.add_argument('--api-url', type=str, default='https://info-beamer.com/api/v1/', help='API URL.')
args = parser.parse_args()

InfobeamerAPI.KEY = os.environ.get('API_KEY') or args.api_key
InfobeamerAPI.URL = os.environ.get('API_URL') or args.api_url
InfobeamerAPI.USER = os.environ.get('API_USER') or args.api_user

if __name__ == '__main__':
    ibh = Infobeamer()
