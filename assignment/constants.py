'''
Created on 11-Mar-2021

@author: dhiraj
'''


from collections import namedtuple


base_path = "/home/dhiraj"
MapTo = namedtuple('MapTo', 'url_type, url, join_on, file_name')

urls = {
        'comments':MapTo('comments', "https://jsonplaceholder.typicode.com/comments", "postId", "/home/dhiraj/comments.csv"),
        "posts": MapTo('posts', "https://jsonplaceholder.typicode.com/posts", "id", "/home/dhiraj/posts.csv")
    }

data_dict = {"comments": ("https://jsonplaceholder.typicode.com/comments", 'postId'), "posts": "https://jsonplaceholder.typicode.com/posts"}