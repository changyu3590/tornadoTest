#-*- coding:utf-8 -*-

import os

import sys
import tornado
from tornado import concurrent

from libs.confUtil import config

port=int(config('system','port'))

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

def run_main():
    urls=autoLoad()
    app = tornado.web.Application(handlers=urls)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as executor:
        executor.submit(run_main)
