#!/usr/bin/env python
# coding: utf-8

import configparser
import sys
config = configparser.ConfigParser()
rootPath = sys.argv[1]
config['DEFAULT']['ROOT'] =  rootPath
with open('configure.ini', 'w') as configfile:
    config.write(configfile)

