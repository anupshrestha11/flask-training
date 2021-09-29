from flask_mongoengine import MongoEngine
from flask_restful import Api
import redis

db = MongoEngine()
api = Api()
r = redis.Redis()
