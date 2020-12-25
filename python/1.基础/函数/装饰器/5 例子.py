#python3.7
#Filename:例子.py

#使用了多个装饰器，不同条件执行不同功能
"""
需求: 判断登陆用户是否未管理员is_admin(此处管理员只有一个为：admin用户)
      1).如果用户为管理员, 则执行被装饰的函数；
      2).如果用户不是管理员, 则报错。
"""

import functools
login_users = ["admin","root"]

def is_admin(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if kwargs.get("name")=="admin":
            res = func(*args,**kwargs)
        else:
            res = "Error，没有权限"
        return res
    return wrapper

def is_login(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if kwargs.get("name") in login_users:
            res = func(*args,**kwargs)
        else:
            res = login()
        return res
    return wrapper

@is_login           #重点：顺序。先判断账号是否在users列表内，是的话再判断是否为“admin”
@is_admin           #需要结合两个装饰器中的封装器功能判断顺序
def write(name):
    return "编写博客"

def login():
    return "账号错误，重新登陆"

print(write(name="admin"))
print('\n')
print(write(name="root"))
print('\n')
print(write(name="admin66"))
            
