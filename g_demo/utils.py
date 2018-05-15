from flask import g

def login_log():
    print('当前登录用户为: %s' % g.username)