from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.task_service import TaskService
from models.task import Task

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    TaskService.create_task(name, description)
    return redirect(url_for('tasks.index'))

@task_blueprint.route('/tasks/<int:task_id>', methods=['POST'])
def update_task(task_id):
    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    updated_task = TaskService.update_task(task_id, name, description)
    if not updated_task:
        return jsonify({'error': 'Task not found'}), 404

    return redirect(url_for('tasks.index'))

@task_blueprint.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)