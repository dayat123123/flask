from flask import Flask, jsonify, request
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
import os
# koneksi database
import mysql.connector
from flask_pymysql import MySQL
# app = Flask(__name__)
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
