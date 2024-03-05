from flask_sqlalchemy import SQLAlchemy 
import json

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False)
    votes = db.Column(db.Integer, nullable=False, default=0)


def connect_to_db(flask_app, db_uri="postgresql://bbrbr:9822@localhost:5432/polls2", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")



if __name__ == "__main__":
    from server import app

    with app.app_context(): 
        connect_to_db(app)
  