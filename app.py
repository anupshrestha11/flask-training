from flask import Flask, jsonify, request

todos = [{
    "id" : 1,
    "title": "Clean PC",
    "description": "removing dusts from the Pc an keep is shining",
    "status": "in-complete",
}]

app = Flask(__name__)


@app.route("/todos", methods=["GET"])
def get_all_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def add_new_todo():
    new_todo = {
        "id" : len(todos) + 1,
        "title": request.json['title'],
        "status": request.json['status'],
        "description": request.json['description']
    }
    todos.append(new_todo)
    return jsonify(new_todo)


app.run(port=8080, debug=True)
