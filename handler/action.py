# /usr/bin/python2
# -*- coding:utf-8 -*-
import Tkinter


class App(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.create_panel()

    def create_panel(self):
        tk = Tkinter.Tk()
        tk.title = 'wantDo'
        tk.geometry('{}x{}'.format(self.width, self.height))
        tk.mainloop()

    def add_todo(self):
        '''
        添加需要做的事情
        :return:
        '''
        pass

    def show_todo(slef):
        '''
        展示需要做的事情
        :return:
        '''
        pass

    def del_todo(self):
        pass

    def save_db(self):
        '''
        保存数据到db
        :return:
        '''
        pass