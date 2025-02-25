from flask import Flask
from app.routes.analysis_api import analysis_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(analysis_bp)
    
    return app