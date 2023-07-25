from flask import Flask
from flask_mysql import MySQL

api = Flask(__name__)
api.config['MYSQL_HOST'] = '<host>'
api.config["MYSQL_PORT"] = '<port>'
api.config['MYSQL_USER'] = '<user>'
api.config['MYSQL_PASSWORD'] = '<password>'
api.config['MYSQL_DB'] = '<database>'

db = MySQL(api)