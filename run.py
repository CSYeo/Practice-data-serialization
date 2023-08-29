#! /usr/bin/env python3

import os
#import requests

directory = "{}\\data\\feedback".format(os.getcwd())

posts = []

for file in os.listdir(directory):
    #print(file)
    #Here remember to use os.listdir if not it will
    #print directory as a string

    filepath = "{}\\{}".format(directory, file)

    with open(filepath, 'r') as data:
        lines = data.readlines()
#lines now will read one line at a time
        title = lines[0].strip()
        name = lines[1].strip()
        date = lines[2].strip()
        feedback = lines[3:].strip()

        dict = {
        "title": title,
        "name": name,
        "date": date,
        "feedback": feedback
        }

    post.append(dict)

print[post]
