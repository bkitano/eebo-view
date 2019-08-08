from app import app
from flask import request
from btest import model_view_topic

@app.route('/')

@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/topic')
def login():
    topic = request.args.get('topic')
    a = model_view_topic(int(topic))
    return a