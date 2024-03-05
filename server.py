from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify, make_response
from model import connect_to_db
from flask_cors import CORS, cross_origin
from pusher import pusher
import simplejson
from crud import select_all_items, update_item
from jinja2 import StrictUndefined
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
pusher_client = pusher.Pusher(app_id='1766209',
  key='14d84efd78f74fc17e49',
  secret='14ff5da946ce15905a3d',
  cluster='mt1',
  ssl=True
)
app.secret_key = os.environ['SECRET_KEY']
app.jinja_env.undefined = StrictUndefined

def main():
	global conn, c
	
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/vote', methods=['POST'])
def vote():
	data = simplejson.loads(request.data)
	update_item([data['member']])
	output = select_all_items([data['member']])
	pusher.trigger(u'poll', u'vote', output)
	return request.data


pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True)




