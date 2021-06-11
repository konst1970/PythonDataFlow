from flask import Flask, escape, url_for, jsonify, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(name="microservice is ready")

@app.route('/run')
def run():
    address = os.environ.get('DATAFLOW')
    res = requests.post(address, json={"text1": "Hello ", "text2": "World"})
    return jsonify(name=res.text)


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    req_data = request.get_json()
    w1 = req_data['text1']
    w2 = req_data['text2']
    return w1+w2