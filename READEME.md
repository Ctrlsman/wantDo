## 环境
Python 3.X
Mysql >= 5.7


## 运行
```shell
git clone https://github.com/Ctrlsman/wantDo.git
mysql -u用户名 -p密码 数据库 < 要导入的数据库数据(schema.sql)
settings.py文件中设置你的数据库信息
pip install -r requirements.txt
python app.py
```

## 测试

浏览器打开:http://localhost:5000