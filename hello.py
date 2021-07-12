from flask import Flask
from flask import jsonify
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/on')
def on():
   return "ON"

@app.route('/off')
def off():
   return "OFF"

@app.route('/data')
def data():
   ret = {
      "temperature": str(random.randrange(0,50)),
      "humidity": str(random.randrange(0,100))
   }
   return jsonify(ret)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)