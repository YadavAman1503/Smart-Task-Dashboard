from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from config import Config

db = SQLAlchemy()

socketio = SocketIO(
    cors_allowed_origins="*"
)

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    socketio.init_app(app)

    from app.routes.task_routes import task_bp
    from app.routes.auth_routes import auth_bp

    app.register_blueprint(task_bp)

    app.register_blueprint(auth_bp)

    return app