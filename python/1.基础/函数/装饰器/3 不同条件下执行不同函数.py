#python3.7
#Filename:不同条件下执行不同函数.py

import functools

login_users = ['admin','root']      #允许的用户名列表

def is_login(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):    #name="admin"，kwargs={"name":"admin"}
        #判断用户是否登陆成功
        if kwargs.get("name") in login_users:   #判断该用户名是否在允许的用户名列表
            res = func(*args,**kwargs)
        else:
            res = login()
        return res
    return wrapper

#必须登陆成功
@is_login
def writeBlog(name):
    return "编写博客"

def login():
    return "重新登陆..."

#无论是否登陆成功都可以执行的代码
def news():
    print("新闻......")

print(writeBlog(name="admin"))      #登陆成功。此时的writeBlog是装饰器函数，所以可以用关键字参数
print("\n\n")
print(writeBlog(name="admin66"))    #登陆不成功


