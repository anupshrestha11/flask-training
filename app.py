from flask import Flask

from extensions import db
from routes import api_routes_blueprint

database_name = "flask_training"

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": database_name
}

db.init_app(app)
app.register_blueprint(api_routes_blueprint)

app.run(port=8080, debug=True)
