from ..db import db

class Journal(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  date = db.Column(db.Date, nullable=False)
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())