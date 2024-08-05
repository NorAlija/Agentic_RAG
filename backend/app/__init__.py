from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Enable CORS to communicate with the frontend. Frontend runs on port 3000 and backend on 5000
    # CORS enables them to communicate with eachother
    CORS(app)

    # Load configurations from .env
    app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'data')

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
