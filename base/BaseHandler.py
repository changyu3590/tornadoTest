# -*- coding:utf-8 -*-
import traceback

import tornado
from tornado import web

from base.Async import async


class BaseHandler(web.RequestHandler):

    def write_error(self, status_code, **kwargs):
        super(BaseHandler).write_error(status_code, **kwargs)

    def prepare(self):
        print('*IP:%s\n*URI:%s\n*METHOD:%s' % (
        self.request.remote_ip, self.request.uri, self.request.method))

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args):
        try:
            yield async.cmd(self._get, *args)
        except ValueError as e:
            print(traceback.format_exc())
            self.execpt(e.message)
        except NotImplementedError as e:
            self.execpt(e.message)
        except Exception as e:
            self.execpt(traceback.format_exc())

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args):
        try:
            yield async.cmd(self._post, *args)
        except ValueError as e:
            print(traceback.format_exc())
            self.execpt(e.message)
        except NotImplementedError as e:
            self.execpt(e.message)
        except Exception as e:
            self.execpt(traceback.format_exc())

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def put(self, *args):
        try:
            yield async.cmd(self._put, *args)
        except ValueError as e:
            print(traceback.format_exc())
            self.execpt(e.message)
        except NotImplementedError as e:
            self.execpt(e.message)
        except Exception as e:
            self.execpt(traceback.format_exc())

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def delete(self, *args):
        try:
            yield async.cmd(self._delete, *args)
        except ValueError as e:
            print(traceback.format_exc())
            self.execpt(e.message)
        except NotImplementedError as e:
            self.execpt(e.message)
        except Exception as e:
            self.execpt(traceback.format_exc())

    def execpt(self, message):
        res = {
            'fun': self.request.uri,
            'method':self.request.method,
            'remote_host': self.request.host,
            'remote_ip': self.request.remote_ip,
            'return_code': -1,
            'sub_msg': message
        }
        self.finish(res)
        return

    def httpResponse(self, message):
        res = {
            'fun': self.request.uri,
            'method': self.request.method,
            'remote_host': self.request.host,
            'remote_ip': self.request.remote_ip,
            'retrun_code': 1,
            'return_result': message
        }
        self.finish(res)
        return

    def _get(self, *args):
        raise NotImplementedError(u"暂无此操作")

    def _put(self, *args):
        raise NotImplementedError(u"暂无此操作")

    def _delete(self, *args):
        raise NotImplementedError(u"暂无此操作")

    def _post(self, *args):
        raise NotImplementedError(u"暂无此操作")

