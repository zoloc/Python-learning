import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlktqa_demo'
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'init#201605'
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
