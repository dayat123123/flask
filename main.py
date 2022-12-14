from flask import Flask, jsonify
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"HIDAYATULLAH": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run()
