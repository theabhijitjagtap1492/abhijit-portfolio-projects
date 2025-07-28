import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize extensions
db = SQLAlchemy()

def create_app(config_name='default'):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.abspath(os.path.join(base_dir, '..', 'templates'))
    static_dir = os.path.abspath(os.path.join(base_dir, '..', 'static'))

    app = Flask(
        __name__,
        template_folder=template_dir,
        static_folder=static_dir
    )
    
    # Import configuration
    from config import config
    app.config.from_object(config[config_name])
    
    # Initialize extensions with app
    db.init_app(app)
    
    # Import and register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app 