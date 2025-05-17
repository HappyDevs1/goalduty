from ..db import db

class AIMessages(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  messages = db.Column(db.JSON, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)