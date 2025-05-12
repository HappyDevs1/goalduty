from flask import jsonify, request
from ..models.user_model import User
from ..db import db

def get_all_users():
  users = User.query.all()
  return jsonify([{
    'id': user.id,
    'name': user.name,
    'email': user.email
  } for user in users]), 200

def get_user_by_id(user_id):
  user = User.query.get(user_id)

  if not user:
    return jsonify({'message': 'User not found'}), 404
  
  return jsonify({
    'id': user.id,
    'name': user.name,
    'email': user.email
  }), 200

def create_user():
  data = request.get_json()

  if not data or 'name' not in data or 'email' not in data:
    return jsonify({'message': 'Invalid input'}), 400
  
  if User.query.filter_by(email=data['email']).first():
    return jsonify({'message': 'Email already exists'}), 400
  
  new_user = User(name=data['name'], email=data['email'])

  db.session.add(new_user)
  db.session.commit()

  return jsonify({
    'id': new_user.id,
    'name': new_user.name,
    'email': new_user.email
  }), 201

def update_user(user_id):
  user = User.query.get(user_id)

  if not user:
    return jsonify({'message': 'User not found'}), 404
  
  data = request.get_json()

  if not data:
    return jsonify({'message': 'Invalid input'}), 400
  
  if 'name' in data:
    user.name = data['name']
  
  if 'email' in data:
    user.email = data['email']

  db.session.commit()

  return jsonify({
    'id': user.id,
    'name': user.name,
    'email': user.email
  }), 200

def delete_user(user_id):
  user = User.query.get(user_id)

  if not user:
    return jsonify({'message': 'User not found'}), 404
  
  db.session.delete(user)
  db.session.commit()

  return jsonify({'message': 'User deleted successfully'}), 200