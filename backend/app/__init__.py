from flask import Flask
from .db import db
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)

  from .models import user_model, future_goals_model, daily_tasks_model, daily_report_model, user_messages_model, ai_messages_model
  with app.app_context():
    db.create_all()
  
  from .routes.user_route import user_bp
  from .routes.future_goals_route import future_goals_bp
  from .routes.daily_tasks_route import daily_tasks_bp
  from .routes.daily_report_route import daily_report_bp
  from .routes.ai_model_route import ai_bp
  from .routes.journal_routes import journal_bp
  from .routes.store_audio_route import store_audio_bp
  # Add recommendation routes if necessary

  app.register_blueprint(user_bp, url_prefix='/api/users')
  app.register_blueprint(future_goals_bp, url_prefix='/api/future_goals')
  app.register_blueprint(daily_tasks_bp, url_prefix='/api/daily_tasks') 
  app.register_blueprint(daily_report_bp, url_prefix='/api/daily_reports')
  app.register_blueprint(ai_bp, url_prefix='/api/ai')
  app.register_blueprint(journal_bp, url_prefix='/api/journal')
  app.register_blueprint(store_audio_bp, url_prefix='/api/store_audio')
  # Register recommendation routes if necessary

  return app