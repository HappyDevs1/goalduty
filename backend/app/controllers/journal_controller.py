from flask import request, jsonify
from ..models.journal_model import Journal
from ..db import db

def get_all_journals():
    journals = Journal.query.all()
    return jsonify([{
        'id': journal.id,
        'title': journal.title,
        'content': journal.content,
        'user_id': journal.user_id
    } for journal in journals]), 200

def get_journal_by_id(journal_id):
    journal = Journal.query.get(journal_id)

    if not journal:
        return jsonify({'message': 'Journal not found'}), 404
    
    return jsonify({
        'id': journal.id,
        'title': journal.title,
        'content': journal.content,
        'user_id': journal.user_id
    }), 200

def create_journal():
    data = request.get_json()

    if not data or 'title' not in data or 'content' not in data or 'user_id' not in data:
        return jsonify({'message': 'Invalid input'}), 400
    
    new_journal = Journal(title=data['title'], content=data['content'], user_id=data['user_id'])

    db.session.add(new_journal)
    db.session.commit()

    return jsonify({
        'id': new_journal.id,
        'title': new_journal.title,
        'content': new_journal.content,
        'user_id': new_journal.user_id
    }), 201

def update_journal(journal_id):
    journal = Journal.query.get(journal_id)

    if not journal:
        return jsonify({'message': 'Journal not found'}), 404
    
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Invalid input'}), 400

    if 'title' in data:
        journal.title = data['title']

    if 'content' in data:
        journal.content = data['content']

    db.session.commit()

    return jsonify({
        'id': journal.id,
        'title': journal.title,
        'content': journal.content,
        'user_id': journal.user_id
    }), 200

def delete_journal(journal_id):
    journal = Journal.query.get(journal_id)

    if not journal:
        return jsonify({'message': 'Journal not found'}), 404
    
    db.session.delete(journal)
    db.session.commit()

    return jsonify({'message': 'Journal deleted successfully'}), 200

def get_journals_by_user_id(user_id):
    journals = Journal.query.filter_by(user_id=user_id).all()

    if not journals:
        return jsonify({'message': 'No journals found for this user'}), 404
    
    return jsonify([{
        'id': journal.id,
        'title': journal.title,
        'content': journal.content,
        'user_id': journal.user_id
    } for journal in journals]), 200