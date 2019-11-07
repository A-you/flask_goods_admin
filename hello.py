# encoding: utf-8

"""
@author: you
@site: 
@time: 2019/11/7 14:13
"""
from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
# SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/mysql'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
@app.route('/')
def hello_word():
	from sqlalchemy import text
	sql = text("SELECT * FROM `user`")
	#连接mysql，获取到引擎后执行sql语句
	results = db.engine.execute(sql)
	for row in results:
		#用Log来输出
		app.logger.info(row)
	return "hello world"
if __name__ =="__main__":
	app.run(debug=True)