from flask import jsonify, request
from ..models.future_goals_model import FutureGoal
from ..db import db

def get_all_future_goals():
  future_goals = FutureGoal.query.all()
  return jsonify([{
    'id': id,
    'name': name,
    'user_id': user_id
  } for id, name, user_id in future_goals]), 200

def get_future_goal_by_id(future_goal_id):
  future_goal = FutureGoal.query.get(future_goal_id)

  if not future_goal:
    return jsonify({'message': 'Future goal not found'}), 404
  
  return jsonify({
    'id': future_goal.id,
    'name': future_goal.name,
    'user_id': future_goal.user_id
  }), 200

def create_future_goal():
  data = request.get_json()

  if not data or 'name' not in data or 'user_id' not in data:
    return jsonify({'message': 'Invalid input'}), 400
  
  new_future_goal = FutureGoal(name=data['name'], user_id=data['user_id'])

  db.session.add(new_future_goal)
  db.session.commit()

  return jsonify({
    'id': new_future_goal.id,
    'name': new_future_goal.name,
    'user_id': new_future_goal.user_id
  }), 201

def update_future_goal(future_goal_id):
  future_goal = FutureGoal.query.get(future_goal_id)

  if not future_goal:
    return jsonify({'message': 'Future goal not found'}), 404
  
  data = request.get_json()

  if not data or 'name' not in data or 'user_id' not in data:
    return jsonify({'message': 'Invalid input'}), 400
  
  future_goal.name = data['name']
  future_goal.user_id = data['user_id']

  db.session.commit()

  return jsonify({
    'id': future_goal.id,
    'name': future_goal.name,
    'user_id': future_goal.user_id
  }), 200

def delete_future_goal(future_goal_id):
  future_goal = FutureGoal.query.get(future_goal_id)

  if not future_goal:
    return jsonify({'message': 'Future goal not found'}), 404
  
  db.session.delete(future_goal)
  db.session.commit()

  return jsonify({'message': 'Future goal deleted successfully'}), 200

def get_future_goals_by_user_id(user_id):
  future_goals = FutureGoal.query.filter_by(user_id=user_id).all()

  if not future_goals:
    return jsonify({'message': 'No future goals found for this user'}), 404
  
  return jsonify([{
    'id': future_goal.id,
    'name': future_goal.name,
    'user_id': future_goal.user_id
  } for future_goal in future_goals]), 200
