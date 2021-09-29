from extensions import db


class Todo(db.Document):
    title = db.StringField()
    description = db.StringField()
    status = db.StringField()
