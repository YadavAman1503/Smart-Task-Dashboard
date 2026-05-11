from app import create_app, db, socketio

from app.models.user import User
from app.models.task import Task

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    socketio.run(app, debug=True)