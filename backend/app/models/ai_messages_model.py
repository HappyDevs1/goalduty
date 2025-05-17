from ..db import db

class AIMessages(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_question = db.Column(db.Text, nullable=False)
  second_question = db.Column(db.Text)
  third_question = db.Column(db.Text)
  fourth_question = db.Column(db.Text)
  fifth_question = db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForegnKey('user.id'), nullable=False)