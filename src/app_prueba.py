import flask
import json
from flask import Flask
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

""" { "label": "My second task", "done": false }
al ingresar estos datos en el insomnia para hacer POST, 
False deberia ir si o si en minuscula, de otra forma
tirara error json.decoder.JSONDecodeError """

Ejercicio 3.3
@app.route('/todos', methods=['GET'])
def hello_world():
    
    return "<h1>Hello!</h1>

Ejercicio 7.0
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
    


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)