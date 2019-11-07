# encoding: utf-8

"""
@author: you
@site: 
@time: 2019/11/7 15:05
"""
from application import app

from web.contronllers.index import index_route

app.register_blueprint(index_route,url_prefix='/index')