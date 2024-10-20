from flask import Flask, jsonify
from src.views.users_routes import user_blueprint
from src.models.model import db
from src.config.config import Config
from flask_jwt_extended import JWTManager
import os




app = Flask(__name__)
app.config.from_object(Config)
app_context = app.app_context()
app_context.push()
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key_here'
db.init_app(app)
jwt = JWTManager(app)
db.create_all()

app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)