from ..db import db

class FutureGoal(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(500), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)