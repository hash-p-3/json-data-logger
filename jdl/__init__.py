"""jdl module: json-data-logger"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_programmer():
    return 'Welcome to "Start to Program!"'
