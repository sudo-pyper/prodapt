'''
Created on 11-Mar-2021

@author: dhiraj
'''
import os
import logging

logger = logging.getLogger(__name__)

from assignment.constants import urls
from assignment.constants import base_path
from assignment.file_writer import FileWriter
from assignment.joiner import Joiner
from assignment.json_parser import JsonParser


def create_unified_csv_file():

    logging.info('Starting url fetch')

    for key in urls:
        url = urls[key].url
        file_name = os.path.join(base_path,urls[key].file_name)

        json_obj = JsonParser(url)
        json_data = json_obj.parse_url()
        file_obj = FileWriter(json_data, file_name)
        file_obj.write_file()
        logging.info('Generated csv file for {}'.format(file_name))

    comments_join_on = urls['comments'].join_on
    comments_file_name = urls['comments'].file_name
    posts_join_on = urls['posts'].join_on
    posts_file_name = urls['posts'].file_name

    output_file_name = os.path.join(base_path, "combined.csv")
    joiner = Joiner(comments_file_name, posts_file_name, comments_join_on, posts_join_on, output_file_name)
    joiner.join()
    logging.info(' Generated combibed csv file for comments and posts. Output file name {}'.format(output_file_name))
    print(' Generated combibed csv file for comments and posts. Output file name {}'.format(output_file_name))

if __name__ == "__main__":
    create_unified_csv_file()
