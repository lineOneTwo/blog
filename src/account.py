import datetime
from utils.db import Connect


def login(username, password):
    with Connect as conn:
        sql = "select id,nickname from user where username=%(username)s and password=%(password)s"
        result = conn.fetch_one(sql, username=username, password=password)
        return result


def register(user, pwd, nickname, mobile, email):
    with Connect as conn:
        sql = 'insert into user(username,pwd,nickname,mobile,email,ctime) values(%s,%s,%s,%s,%s)'
        result = conn.fetch_one(sql, user, pwd, nickname, mobile, email)
        return result
