from flask import Flask, jsonify, request, g
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
import os

# koneksi database
import pymysql 
from flask_pymysql import MySQL
import pymysql.cursors

# Connect to the database
# connection = pymysql.connect(host='sql6.freemysqlhosting.net',
#                              user='sql6513279',
#                              password='71TDCiXpb4',
#                              database='sql6513279',
#                              cursorclass=pymysql.cursors.DictCursor)
def connection():
  host='sql6.freemysqlhosting.net'
  user='sql6513279'
  password='71TDCiXpb4'
  database='sql6513279'
  conn = pymysql.connect(host=host, user=user, password=password, database=database)
  return conn

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:AOIo6SOBjx83a5ly13Pn@containers-us-west-180.railway.app:7485/railway'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

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
    global banjarindo
    aa = "ulun"
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT kata_dasar FROM tb_katadasar2 where kata_daerah = %s", [aa])
    banjarindo = cursor.fetchone()[0]
    ada = translator.translate(aa, dest='en')
    answer= banjarindo
    return answer
# api 1 
@app.route('/api1', methods = ['GET'])
def returnvalue1():
    global indoinggris
    d = {}
    inputchr = str(request.args['query'])
    indoinggris = translator.translate(inputchr, dest='en')
    answer = indoinggris.text
    d['output'] = answer
    return d
  
#   api 2
@app.route('/api2', methods = ['GET'])
def returnvalue2():
    global inggrisindo
    d = {}
    inputchr = str(request.args['query'])
    inggrisindo = translator.translate(inputchr, dest='id')
    answer = inggrisindo.text
    d['output'] = answer
    return d
  
#   api 3
@app.route('/api3', methods = ['GET'])
def returnvalue3():
#     global banjarindo
#     d = {}
#     inputchr = str(request.args['query'])
#     conn = connection()
#     cursor = conn.cursor()
#     row_count = cur.execute("SELECT kata_dasar FROM tb_katadasar2 where kata_daerah = %s", [inputchr])
#     conn.connection.commit()
#     if row_count > 0:
#         banjarindo=cur.fetchone()[0]
#         answer = banjarindo
#         d['output'] = answer
#         return d
#     else:
#         hasil = "Kata belum tersedia"
#         d['output'] = hasil
#         return d
      global banj
      conn2 = pymysql.connect(host='sql6.freemysqlhosting.net', user='sql6513279', password='71TDCiXpb4', database='sql6513279')
      cursor2 = conn2.cursor()
      my_list = []
      d= {}
      string = str(request.args['query'])
      list_string = string.split()
      n = len(list_string)
#       for i in range(n):
#           try:
#             cursor.execute("SELECT kata_dasar FROM tb_katadasar2 where kata_daerah = %s", [list_string[i]])
#             banj=cur.fetchone()[0]
#             answer = banj
#             my_list.append(answer)
#           except:
#             my_list.append(list_string[i])
#       d['output'] = ' '.join(my_list)
#       return d
        for i in range(n):
        row_count = cursor2.execute("SELECT kata_dasar FROM tb_katadasar2 where kata_daerah = %s", [list_string[i]])
        conn2.commit()
        if row_count > 0:
            banj=cursor2.fetchone()[0]
            answer = banj
            my_list.append(answer)
        else:
            my_list.append(list_string[i])

    d['output'] = ' '.join(my_list)
    return d
  
#   batas api yang dipakai
# @app.route('/api22', methods = ['GET'])
# def returnvalue22():
#     global hasilbanjar
#     d = {}
#     inputchr = str(request.args['query'])
#     hasilbanjar = translator.translate(inputchr, dest='en')
#     answer = hasilbanjar.text
#     d['output'] = answer
#     return d
 
# @app.route('/api23', methods = ['GET'])
# def returnvalue23():
#     global indo
#     d = {}
#     inputchr = str(request.args['query'])
#     conn = connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT kata_daerah FROM tb_katadasar2 where kata_dasar = %s", [inputchr])
#     indo = cursor.fetchone()[0]
#     answer= indo
#     return answer

# tutup route api


if __name__ == '__main__':
    app.run()
