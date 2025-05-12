from flask import Flask
from .db import db
from .routes import api_bp
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)

  from .models import user_model, future_goals_model, daily_tasks_model, daily_reports_model
  with app.app_context():
    db.create_all()
  
  from .routes import user_bp
  from .routes import future_goals_bp
  from .routes import daily_tasks_bp
  from .routes import daily_reports_bp
  # Add recommendation routes if necessary

  app.register_blueprint(user_bp, url_prefix='/api/users')
  app.register_blueprint(future_goals_bp, url_prefix='/api/future_goals')
  app.register_blueprint(daily_tasks_bp, url_prefix='/api/daily_tasks') 
  app.register_blueprint(daily_reports_bp, url_prefix='/api/daily_reports')
  # Register recommendation routes if necessary
  
  return app