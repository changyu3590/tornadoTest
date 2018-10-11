#-*- coding:utf-8 -*-
import configparser
import os

config_util = configparser.ConfigParser()

_root=os.path.dirname(os.path.dirname(__file__))


def dbconfig(option, key):

    config_util.read(_root+'\\config\\db.conf')

    return config_util.get(option, key)

def config(option, key):

    config_util.read(_root+'\\config\\base.conf')

    return config_util.get(option, key)