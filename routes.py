from flask import Blueprint

from extensions import api
from resources.todo_resources import TodoController, TodoListController

api_routes_blueprint = Blueprint("api_routes_blueprint", __name__)

api.init_app(api_routes_blueprint)

api.add_resource(TodoListController, "/todos")
api.add_resource(TodoController, "/todos/<string:todo_id>")
