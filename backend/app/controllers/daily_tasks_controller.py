from flask import jsonify, request
from ..models.daily_tasks_model import DailyTask
from ..db import db

def get_all_daily_tasks():
    daily_tasks = DailyTask.query.all()
    return jsonify([{
        'id': task.id,
        'name': task.name,
        'user_id': task.user_id
    } for task in daily_tasks]), 200

def get_daily_task_by_id(daily_task_id):
    daily_task = DailyTask.query.get(daily_task_id)

    if not daily_task:
        return jsonify({'message': 'Daily task not found'}), 404
    
    return jsonify({
        'id': daily_task.id,
        'name': daily_task.name,
        'user_id': daily_task.user_id
    }), 200

def create_daily_task():
    data = request.get_json()

    if not data or 'name' not in data or 'user_id' not in data:
        return jsonify({'message': 'Invalid input'}), 400
    
    new_daily_task = DailyTask(name=data['name'], user_id=data['user_id'])

    db.session.add(new_daily_task)
    db.session.commit()

    return jsonify({
        'id': new_daily_task.id,
        'name': new_daily_task.name,
        'user_id': new_daily_task.user_id
    }), 201

def update_daily_task(daily_task_id):
    daily_task = DailyTask.query.get(daily_task_id)

    if not daily_task:
        return jsonify({'message': 'Daily task not found'}), 404
    
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Invalid input'}), 400

    if 'name' in data:
        daily_task.name = data['name']

    if 'user_id' in data:
        daily_task.user_id = data['user_id']

    if 'non_negotiable' in data:
        daily_task.non_negotiable = data['non_negotiable']

    db.session.commit()

    return jsonify({
        'id': daily_task.id,
        'name': daily_task.name,
    }), 200

def delete_daily_task(daily_task_id):
    daily_task = DailyTask.query.get(daily_task_id)

    if not daily_task:
        return jsonify({'message': 'Daily task not found'}), 404
    
    db.session.delete(daily_task)
    db.session.commit()

    return jsonify({'message': 'Daily task deleted successfully'}), 200

def mark_daily_task_completed(daily_task_id):
    daily_task = DailyTask.query.get(daily_task_id)

    if not daily_task:
        return jsonify({'message': 'Daily task not found'}), 404
    
    daily_task.completed = True
    db.session.commit()

    return jsonify({
        'id': daily_task.id,
        'name': daily_task.name,
        'user_id': daily_task.user_id,
        'completed': daily_task.completed
    }), 200

def get_daily_tasks_by_user(user_id):
    daily_tasks = DailyTask.query.filter_by(user_id=user_id).all()

    if not daily_tasks:
        return jsonify({'message': 'No daily tasks found for this user'}), 404
    
    return jsonify([{
        'id': task.id,
        'name': task.name,
        'user_id': task.user_id
    } for task in daily_tasks]), 200