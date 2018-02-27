# /usr/bin/python2
# -*- coding:utf-8 -*-
# 一个todolist小程序,将需要做的事情写在里面,每天开机自动弹窗提醒

import pymysql

from config import dev
from handler import action

mysql_conn = pymysql.connect(**dev.mysql_cfg)
cur = mysql_conn.cursor()

app = action.App(200, 150)