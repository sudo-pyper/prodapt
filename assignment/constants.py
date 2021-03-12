'''
Created on 11-Mar-2021

@author: dhiraj
'''


from collections import namedtuple
import os

base_path = "/home/dhiraj/prodapt/assignment/output_files"
MapTo = namedtuple('MapTo', 'url_type, url, join_on, file_name')

urls = {
        'comments':MapTo('comments', "https://jsonplaceholder.typicode.com/comments", "postId", os.path.join(base_path,"comments.csv")),
        "posts": MapTo('posts', "https://jsonplaceholder.typicode.com/posts", "id", os.path.join(base_path,"posts.csv"))
    }

data_dict = {"comments": ("https://jsonplaceholder.typicode.com/comments", 'postId'), "posts": "https://jsonplaceholder.typicode.com/posts"}
