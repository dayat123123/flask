from flask import Flask, jsonify, request, g
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
import os

# koneksi database
import pymysql 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:AOIo6SOBjx83a5ly13Pn@containers-us-west-180.railway.app:7485/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql6513279:71TDCiXpb4@sql6.freemysqlhosting.net/sql6513279'
# db = SQLAlchemy(app)

# koneksi db
# db = pymysql.connect("sql6.freemysqlhosting.net", "sql6513279", "71TDCiXpb4", "sql6513279")
# batas

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
# app.config['MYSQL_USER'] = 'sql6513279'
# app.config['MYSQL_PASSWORD'] = '71TDCiXpb4'
# app.config['MYSQL_DB'] = 'sql6513279'
# mysql = MySQL(app)
# batas koneksi database

# route api
@app.route('/')
def index():
    aa = "Saya sangat senang karena program saya berjalan, Alhamdulillah ya Allah"
    ada = translator.translate(aa, dest='en')
    answer= ada.text
    return answer

@app.route('/api', methods = ['GET'])
def returnvalue():
    global hasilbanjar
    d = {}
    inputchr = str(request.args['query'])
    hasilbanjar = translator.translate(inputchr, dest='en')
    answer = hasilbanjar.text
    d['output'] = answer
    return d

# tutup route api


if __name__ == '__main__':
    app.run()
