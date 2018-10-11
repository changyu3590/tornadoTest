#-*- coding:utf-8 -*-

import os

import sys
import tornado
from tornado import concurrent

from libs.apsCron import get_scheduler
from libs.confUtil import config

port=str(config('system','port')).split(',')

def autoLoad():
    try:
        pt=os.path.join(os.path.dirname(__file__), "apps")
        apps=os.listdir(pt)
        apps.pop()
        urls=[]
        for _app in apps:
            __import__('apps.%s.handler'%_app)
            module=sys.modules['apps.%s.handler'%_app]
            for _handler in (getattr(module,'handler')):
                urls.append(_handler)
        return urls
    except Exception as e:
        raise ValueError('路由加载失败')

def main(port=None):
    urls=autoLoad()
    app = tornado.web.Application(handlers=urls)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

def cronJob():
    '''定时检查待支付订单'''
    schedule = get_scheduler()
    #schedule.add_job(cron_query, 'interval', seconds=60)
    #schedule.start()

if __name__ == "__main__":
    workers=len(port)
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        for _p in port:
            executor.submit(main,int(_p))
        executor.submit(cronJob())
