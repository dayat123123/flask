from flask import Flask, jsonify
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
import os

app = Flask(__name__)


@app.route('/')
def index():
    aa = "Saya sangat senang karena program saya berjalan, Alhamdulillah ya Allah"
    ada = translator.translate(aa, dest='en')
    answer= ada.text
    return jsonnify({answer})


if __name__ == '__main__':
    app.run()
