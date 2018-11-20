#-*- coding:utf-8 -*-
import os
'''
生成模组工具类
'''
class Manager():
    def __init__(self):
        self._root=os.path.join(os.path.dirname(__file__),"apps")
        self._templete=os.path.join(os.path.dirname(__file__),"templete")
    def createMoudle(self,name):
        mpath=os.path.join(self._root,name)
        if os.path.exists(mpath):
            raise IOError("[%s]模块已存在" % name)
        else:
            os.makedirs(mpath)
            with open(os.path.join(mpath, '__init__.py'), 'w') as file:
                file.write('#-*- coding:utf-8 -*-')
            with open(os.path.join(mpath,'handler.py'),'w') as file:
                with open(os.path.join(self._templete,'handler.txt'),'r',encoding='utf-8') as _file:
                    while True:
                        code=_file.readline()
                        if code:
                            if code.find('{')>-1:
                                code=code.format(appName=name[0].upper()+str(name[1:]).lower())
                            file.write(code)
                        else:
                            break
            with open(os.path.join(mpath,'models.py'),'w') as file:
                with open(os.path.join(self._templete,'models.txt'),'r',encoding='utf-8') as _file:
                    while True:
                        code=_file.readline()
                        if code:
                            if code.find('{')>-1:
                                code=code.format(appName=name[0].upper()+str(name[1:]).lower())
                            file.write(code)
                        else:
                            break
            with open(os.path.join(mpath,'service.py'),'w') as file:
                with open(os.path.join(self._templete,'service.txt'),'r',encoding='utf-8') as _file:
                    while True:
                        code=_file.readline()
                        if code:
                            if code.find('{')>-1:
                                code=code.format(appName=name[0].upper()+str(name[1:]).lower())
                            file.write(code)
                        else:
                            break
            print ('[%s]模组创建完毕！'%name)

if __name__ == '__main__':
    Manager().createMoudle('test')
