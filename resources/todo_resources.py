from flask import jsonify, request
from flask_restful import Resource
import pickle

from database.todo_docuemnt import Todo
from extensions import r


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
