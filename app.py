from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

todos = [{
    "id": 1,
    "title": "Clean PC",
    "description": "removing dusts from the Pc an keep is shining",
    "status": "in-complete",
}]

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/flask_training"
mongo = PyMongo(app)


@app.route("/todos", methods=["GET"])
def get_all_todos():
    todos = mongo.db.todo
    output = []
    for todo in todos.find():
        output.append({
            'title': todo["title"],
            'description': todo["description"],
            "status": todo["status"]
        })

    return jsonify(output)


@app.route("/todos", methods=["POST"])
def add_new_todo():
    todo = mongo.db.todo
    todo_id = todo.insert_one({
        "title": request.json['title'],
        "status": request.json['status'],
        "description": request.json['description']
    })
    new_todo = todo.find_one({"_id": todo_id})
    output = {
        'title': new_todo["title"],
        'description': new_todo["description"],
        "status": new_todo["status"]
    }
    return jsonify(output)


@app.route("/todos/<title>", methods=["DELETE"])
def delete_todo(title):
    todo = mongo.db.todo
    todo.delete_one({"title": title})
    return ""


@app.route("/todos/<title>", methods=["PUT"])
def update_todos(title):
    todo = mongo.db.todo
    todo_id = todo.update_one({"title": title}, {
        "title": request.json['title'],
        "status": request.json['status'],
        "description": request.json['description']
    })

    return todo_id


app.run(port=8080, debug=True)
