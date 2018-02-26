# /usr/bin/python2
# -*- coding:utf-8 -*-
# 一个todolist小程序,将需要做的事情写在里面,每天开机自动弹窗提醒
from Tkinter import *
import pymysql

from config import dev

root = Tk()

mysql_conn = pymysql.connect(**dev.mysql_cfg)
cur = mysql_conn.cursor()




li = ['C','python','php','html','SQL','java']

listb = Listbox(root)

for item in li:
    listb.insert(0, item)


listb.pack()
root.mainloop()