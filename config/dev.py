# -*- coding:utf-8 -*-
import pymysql

mysql_cfg = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'zds819918',
    'database': 'test',
    'autocommit': True,
    'cursorclass': pymysql.cursors.DictCursor,
}