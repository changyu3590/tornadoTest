#-*- coding:utf-8 -*-

'''实例化APS'''
from apscheduler.schedulers.background import BackgroundScheduler


def get_scheduler():
    scheduler = BackgroundScheduler()
    return scheduler