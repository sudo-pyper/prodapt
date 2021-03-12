'''
Created on 12-Mar-2021

@author: dhiraj
'''

import requests
import json

import logging

logger = logging.getLogger(__name__)

class JsonParser:

    logger.info('Inside json parser class')

    def __init__(self, url):
        self.url = url

    def parse_url(self):
        self.raw_data = requests.get(self.url)
        self.json_data = json.dumps(self.raw_data.json())
        return self.json_data