#!/usr/bin/env python
# encoding:utf8

import os

keywords = ['guige.php', 'shell.php']
syntax = "inurl:"

for keyword in keywords:
    print "==== Searching for '" + keyword + "' ==="
    command = "python ./BaiduAPI.py " + syntax + keyword
    os.system(command)
