from ..db import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(200), nullable=False)
  daily_tasks = db.relationship('DailyTask', backref='user', lazy=True)
  daily_reports = db.relationship('DailyReport', backref='user', lazy=True)
  future_goals = db.relationship('FutureGoal', backref='user', lazy=True)
  # detailed_future_goals = db.Column(db.String(500), nullable=True)