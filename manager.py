# encoding: utf-8

"""
@author: you
@site: 
@time: 2019/11/7 15:05
"""
from application import app,manager
from flask_script import Server #自定义命令
import www
import os

#自定义启动脚本
manager.add_command("runserver",Server(host='0.0.0.0',port=6000,use_debugger=True))
def main():
	app.run(host='0.0.0.0',port=app.config['SERVICE_PORT'])

if __name__=='__main__':
	try:
		import sys
		sys.exit(main())
	except Exception as e:
		import traceback
		traceback.print_exc()