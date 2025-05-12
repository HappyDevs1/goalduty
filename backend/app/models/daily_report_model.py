from ..db import db

class DailyReport(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  tasks_status = db.Column(db.String(500), nullable=False)
  recommendations = db.Column(db.String(500), nullable=True)
  date = db.Column(db.Date, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)