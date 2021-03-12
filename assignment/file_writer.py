'''
Created on 11-Mar-2021

@author: dhiraj
'''

import pandas as pd

import logging

logger = logging.getLogger(__name__)

class FileWriter:

    logger.info('Inside Filewriter class')

    def __init__(self, json_data, file_name):
        self.json_data = json_data
        self.file_name = file_name
        
    def write_file(self):
        df = pd.read_json(self.json_data)
        df.to_csv(self.file_name, index=False)
        return 
