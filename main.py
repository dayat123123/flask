from flask import Flask, jsonify, request
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
import os
import mysql.connector
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql6513279'
app.config['MYSQL_PASSWORD'] = '71TDCiXpb4'
app.config['MYSQL_DB'] = 'sql6513279'
mysql = MySQL(app)

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


@app.route('/api8', methods = ['GET'])
def returnvalue8():
    global banj
    new_string = {}
    my_list = []
    d= {}
    string = str(request.args['query'])
    list_string = string.split()
    n = len(list_string)
    for i in range(n):
        cur = mysql.connection.cursor()
        row_count = cur.execute("SELECT kata_dasar FROM tb_katadasar2 where kata_daerah = %s", [list_string[i]])
        mysql.connection.commit()
        if row_count > 0:
            banj=cur.fetchone()[0]
            answer = banj
            my_list.append(answer)
        else:
            my_list.append(list_string[i])

    d['output'] = ' '.join(my_list)
    return d
# tutup route api


if __name__ == '__main__':
    app.run()
