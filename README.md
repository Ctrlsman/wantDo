## 环境
+ Python 3.X
+ Mysql >= 5.7
+ Flask==0.11.1
+ Flask-Bootstrap==3.3.7.0
+ Flask-Login==0.4.0
+ Flask-SQLAlchemy==2.1
+ Flask-WTF==0.13.1


## 运行
```shell
git clone https://github.com/Ctrlsman/wantDo.git

mysqladmin -u用户名 -密码 create test

mysql -u用户名 -p密码 test < 要导入的数据库数据(schema.sql)

# 注意:建议修改admin密码

settings.py文件中设置你的数据库信息

pip install -r requirements.txt

python app.py

```

## 测试

浏览器打开:http://localhost:5000