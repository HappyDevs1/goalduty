from flask import jsonify, request
from ..models.daily_report_model import DailyReport
from ..db import db

def get_all_daily_reports():
    daily_reports = DailyReport.query.all()
    return jsonify([{
        'id': report.id,
        'user_id': report.user_id,
        'date': report.date,
        'summary': report.summary,
        'task_status': report.task_status,
        'recommendations': report.recommendations
    } for report in daily_reports]), 200

def get_daily_report_by_id(daily_report_id):
    daily_report = DailyReport.query.get(daily_report_id)

    if not daily_report:
        return jsonify({'message': 'Daily report not found'}), 404
    
    return jsonify({
        'id': daily_report.id,
        'user_id': daily_report.user_id,
        'date': daily_report.date,
        'summary': daily_report.summary,
        'task_status': daily_report.task_status,
        'recommendations': daily_report.recommendations
    }), 200

def create_daily_report():
    data = request.get_json()

    if not data or 'user_id' not in data or 'date' not in data or 'report' not in data:
        return jsonify({'message': 'Invalid input'}), 400
    
    new_daily_report = DailyReport(user_id=data['user_id'], date=data['date'], report=data['report'])

    db.session.add(new_daily_report)
    db.session.commit()

    return jsonify({
        'id': new_daily_report.id,
        'user_id': new_daily_report.user_id,
        'date': new_daily_report.date,
        'summary': new_daily_report.summary,
        'task_status': new_daily_report.task_status,
        'recommendations': new_daily_report.recommendations
    }), 201

def update_daily_report(daily_report_id):
    daily_report = DailyReport.query.get(daily_report_id)

    if not daily_report:
        return jsonify({'message': 'Daily report not found'}), 404
    
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Invalid input'}), 400
    
    if 'task_status' in data:
        daily_report.task_status = data['task_status']

    if 'recommendations' in data:
        daily_report.recommendations = data['recommendations']

    db.session.commit()

    return jsonify({
        'id': daily_report.id,
        'user_id': daily_report.user_id,
        'date': daily_report.date,
        'summary': daily_report.summary,
        'task_status': daily_report.task_status,
        'recommendations': daily_report.recommendations
    }), 200

def delete_daily_report(daily_report_id):
    daily_report = DailyReport.query.get(daily_report_id)

    if not daily_report:
        return jsonify({'message': 'Daily report not found'}), 404
    
    db.session.delete(daily_report)
    db.session.commit()

    return jsonify({'message': 'Daily report deleted successfully'}), 200

def get_daily_report_by_user_id(user_id):
    daily_reports = DailyReport.query.filter_by(user_id=user_id).all()

    if not daily_reports:
        return jsonify({'message': 'No daily reports found for this user'}), 404
    
    return jsonify([{
        'id': report.id,
        'user_id': report.user_id,
        'date': report.date,
        'summary': report.summary,
        'task_status': report.task_status,
        'recommendations': report.recommendations
    } for report in daily_reports]), 200