# encoding: utf-8

"""
@author: you
@site: 
@time: 2019/11/7 16:34
"""
from flask import Blueprint

index_route = Blueprint('index',__name__)

@index_route.route('/')
def index():
	return 'index'