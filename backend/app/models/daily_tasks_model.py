from ..db import db

class DailyTask(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  completed = db.Column(db.Boolean, default=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)