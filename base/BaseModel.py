import datetime

from mongoengine import *

from libs.confUtil import _root, dbconfig

database=_root[_root.rfind('\\')+1:]

host=dbconfig('mongo','host')

port=dbconfig('mongo','port')

connect(database, host=host, port=int(port))


class BaseModel(Document):
    # 允许继承
    meta = {'allow_inheritance': True}
    #初始化字段
    add_time = DateTimeField(default=datetime.datetime.now())

    last_updated_time = DateTimeField()
