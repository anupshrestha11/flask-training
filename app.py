from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from flask_restful import Resource, Api
import redis
import pickle

database_name = "flask_training"

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": database_name
}

api = Api(app)

db = MongoEngine(app)

r = redis.Redis()


class Todo(db.Document):
    title = db.StringField()
    description = db.StringField()
    status = db.StringField()


class TodoController(Resource):
    def get(self, todo_id):
        todo = Todo.objects.get_or_404(id=todo_id)
        return jsonify(todo)

    def put(self, todo_id):
        todo = Todo.objects.get_or_404(id=todo_id)
        todo.update(
            title=request.json['title'],
            description=request.json['description'],
            status=request.json['status']
        )
        todo = Todo.objects.get_or_404(id=todo_id)
        r.delete("todos")
        return jsonify(todo)

    def delete(self, todo_id):
        todo = Todo.objects.get_or_404(id=todo_id)
        todo.delete()
        r.delete("todos")
        return jsonify(todo)


class TodoListController(Resource):
    def get(self):
        if r.exists("todos"):
            print("todos already exists")
            return jsonify(pickle.loads(r.get("todos")))
        else:
            print("todos not found")
            todos = Todo.objects()
            r.set("todos", pickle.dumps(todos), px=10000)
            return jsonify(todos)

    def post(self):
        new_todo = Todo(
            title=request.json['title'],
            status=request.json['status'],
            description=request.json['description']
        )
        new_todo.save()
        r.delete("todos")
        return jsonify(new_todo)


api.add_resource(TodoListController, "/todos")
api.add_resource(TodoController, "/todos/<string:todo_id>")


app.run(port=8080, debug=True)
