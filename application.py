# encoding: utf-8

"""
@author: you
@site: 
@time: 2019/11/7 15:05
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os
#为了实现按需加载，定义一个类
class Application( Flask ):
	def __init__(self,import_name):
		super(Application,self).__init__(import_name)
		# if "ops_config" in os.environ:
		# 	self.config.from_pyfile('config/{}_setting.py'.format(os.environ['ops_config']))
		self.config.from_pyfile('config/{}_setting.py'.format('local'))
		db.init_app(self)
db = SQLAlchemy()
app = Application(__name__)

manager = Manager(app)
@app.route('/')
def hello():
	return 'hello'
