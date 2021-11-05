from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from dotenv import dotenv_values

env = dotenv_values(".env")
db_connect_string = "mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
db_connect_string = db_connect_string.format(**env)

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = db_connect_string

db = SQLAlchemy(app)

@dataclass
class User(db.Model):
    id: int
    name: str
    email: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

db.create_all()

# GET
# Listar todos os usuarios
@app.get("/users")
def get_all_users():
    users = User.query.all()
    return jsonify({"users": users}), 200

# Listar usuario especifico
@app.get("/users/<id>")
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if (not user):
        return jsonify({"message": "user not found"}), 404
    return jsonify({"user": user}), 200

# POST
@app.post("/users")
def create_user():
    try:
        body = request.get_json()
        new_user = User(name=body["name"], email=body["email"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "created"}), 201
    except:
        return jsonify({"error": "malformed body"}), 400

# PUT
@app.put("/users/<id>")
def update_user(id):
    user = User.query.filter_by(id=id).first()
    try:
        body = request.get_json()
        if("name" in body):
            user.name = body["name"]
        if("email" in body):
            user.email = body["email"]

        db.session.add(user)
        db.session.commit()
        
        return jsonify({"user": user}), 200
    except:
        return jsonify({"message": "error"}), 400

# DELETE
@app.delete("/users/<id>")
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "deleted with success"}), 200
    except:
        return jsonify({"message": "error"}), 400


if (__name__ == "__main__"):
    app.run()