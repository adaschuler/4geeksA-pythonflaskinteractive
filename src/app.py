import flask
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]



@app.route('/todos', methods=['GET'])
def hello_world():
    global todos
    
    json_text=flask.jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    global todos
    request_body = request.data
    ###print("------------>",request_body)
    decoded_object = json.loads(request_body)
    ###print("------------>",decoded_object)
    todos.append(decoded_object)
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos
    if position <= len(todos):
        todos.pop(position)
    else:
        raise Exception("No existe esta posicion, no puede ser eliminada")
    return jsonify(todos) 


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)