from flask import Flask, jsonify, request
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
import os
app = Flask(__name__)
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
