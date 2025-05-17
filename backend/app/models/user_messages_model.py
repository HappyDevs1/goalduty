from ..db import db

class UserMessages(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_first_message = db.Column(db.Text, nullable=False)
  user_second_message = db.Column(db.Text, nullable=False)
  user_third_message = db.Column(db.Text, nullable=False)
  user_fourth_message = db.Column(db.Text, nullable=False)
  user_fifth_message = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForegnKey('user.id'), nullable=False)