from flask import Blueprint, jsonify, request, render_template
from app import db, socketio
from app.models.task import Task
from app.models.user import User
import pandas as pd
import numpy as np

task_bp = Blueprint("tasks", __name__)


@task_bp.route("/")
def home():
    return render_template("login.html")


@task_bp.route("/login")
def login_page():
    return render_template("login.html")


@task_bp.route("/register")
def register_page():
    return render_template("register.html")


@task_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@task_bp.route("/api/register", methods=["POST"])
def register():

    data = request.json

    existing_user = User.query.filter(
        (User.email == data["email"]) |
        (User.username == data["username"])
    ).first()

    if existing_user:
        return jsonify({
            "success": False,
            "message": "User already exists"
        })

    user = User(
        username=data["username"],
        email=data["email"],
        password_hash=data["password"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Registration Successful"
    })


@task_bp.route("/api/login", methods=["POST"])
def login():

    data = request.json

    user = User.query.filter(
        (User.email == data["email"]) |
        (User.username == data["email"])
    ).first()

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found"
        })

    if user.password_hash != data["password"]:
        return jsonify({
            "success": False,
            "message": "Invalid password"
        })

    return jsonify({
        "success": True,
        "message": "Login Successful"
    })


@task_bp.route("/api/tasks")
def get_tasks():

    tasks = Task.query.all()

    data = []

    for task in tasks:

        data.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status
        })

    return jsonify(data)


@task_bp.route("/api/add-task", methods=["POST"])
def add_task():

    data = request.json

    task = Task(
        title=data["title"],
        description=data["description"],
        priority=data["priority"],
        status="Pending"
    )

    db.session.add(task)
    db.session.commit()

    socketio.emit("task_update", {
        "message": "New Task Added"
    })

    return jsonify({
        "success": True,
        "message": "Task Added"
    })


@task_bp.route("/api/complete-task/<int:id>", methods=["PUT"])
def complete_task(id):

    task = Task.query.get(id)

    if not task:
        return jsonify({
            "success": False,
            "message": "Task not found"
        })

    task.status = "Completed"

    db.session.commit()

    socketio.emit("task_update", {
        "message": "Task Completed"
    })

    return jsonify({
        "success": True,
        "message": "Task Completed"
    })


@task_bp.route("/api/delete-task/<int:id>", methods=["DELETE"])
def delete_task(id):

    task = Task.query.get(id)

    if not task:
        return jsonify({
            "success": False,
            "message": "Task not found"
        })

    db.session.delete(task)

    db.session.commit()

    socketio.emit("task_update", {
        "message": "Task Deleted"
    })

    return jsonify({
        "success": True,
        "message": "Task Deleted"
    })


@task_bp.route("/api/analytics")
def analytics():

    tasks = Task.query.all()

    statuses = [task.status for task in tasks]

    total = len(statuses)

    completed = statuses.count("Completed")

    pending = statuses.count("Pending")

    percentage = 0

    if total > 0:
        percentage = round((completed / total) * 100, 2)

    df = pd.DataFrame({
        "status": statuses
    })

    analytics_data = {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "completion_percentage": percentage,
        "numpy_average": float(np.mean([completed, pending]))
    }

    return jsonify(analytics_data)