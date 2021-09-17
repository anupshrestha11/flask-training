from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine

database_name = "flask_training"

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": database_name
}

db = MongoEngine(app)


class Todo(db.Document):
    title = db.StringField()
    description = db.StringField()
    status = db.StringField()


@app.route("/todos", methods=["GET"])
def get_all_todos():
    todos = Todo.objects()
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def add_new_todo():
    new_todo = Todo(
        title=request.json['title'],
        status=request.json['status'],
        description=request.json['description']
    )
    new_todo.save()
    return jsonify(new_todo)


@app.route("/todos/<id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todo.objects.get_or_404(id=id)
    todo.delete()
    return jsonify(todo)


@app.route("/todos/<id>", methods=["PUT"])
def update_todos(id):
    todo = Todo.objects.get_or_404(id=id)
    todo.update(
        title=request.json['title'],
        description=request.json['description'],
        status=request.json['status']
    )
    todo = Todo.objects.get_or_404(id=id)
    return jsonify(todo)


app.run(port=8080, debug=True)
