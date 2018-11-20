#-*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor

from tornado.concurrent import run_on_executor


class Async():
    def __init__(self):
        # self.io_loop = IOLoop.current()
        self.executor = ThreadPoolExecutor(max_workers=100)

    @run_on_executor
    def cmd(self,func,*args,**kwargs):
        return func(args,**kwargs)

async=Async()