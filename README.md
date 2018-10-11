# 搭建的tornado简单MVC架构
##主要内容：
### 1、一键创建模块
        1.1、包含handler、service、models
    2、MVC说明：
       handler:路由层
       service:业务层
       models:持久层
    3、持久层采用mongoengine，类似django ORM操作。
    4、采用了协程+多线程处理并发业务请求
    5、重写了tornado RequestHandler父类函数：
        5.1、错误跳转处理
        5.2、AOP处理
    6、多模块(handler)路由合并
#此项目作为初学者学习参考使用，如有问题，请喷
