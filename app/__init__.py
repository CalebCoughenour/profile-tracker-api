import os
from flask import Flask
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    from app.main_routes import main
    from app.crypto_routes import crypto
    from app.stock_routes import stocks

    app.register_blueprint(main)
    app.register_blueprint(crypto)
    app.register_blueprint(stocks)

    @app.context_processor
    def inject_current_date():
        return {"current_date": datetime.now().date()}

    return app