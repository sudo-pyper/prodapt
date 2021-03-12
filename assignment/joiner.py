'''
Created on 11-Mar-2021

@author: dhiraj
'''
import pandas as pd

import logging

logger = logging.getLogger(__name__)

class Joiner:

    logger.info('Inside class joiner')

    def __init__(self, left_file, right_file, left_join_col, right_join_col, output_file_name):

        self.left_file = left_file
        self.right_file = right_file
        self.left_join_col = left_join_col
        self.right_join_col = right_join_col
        self.output_file_name = output_file_name 

    def join(self):

        file1 = pd.read_csv(self.left_file)
        file2 = pd.read_csv(self.right_file)
        joined_df = file1.merge(file2, left_on=self.left_join_col, right_on = self.right_join_col)
        joined_df.to_csv(self.output_file_name)
        logger.info('Combined the file {} and {} and created output file {} at'.format(file1,file2, self.output_file_name))