from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import stripe
from config import Config

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
admin = Admin()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.debug = True  # Включение режима отладки

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    admin.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    from app.models import Product, Order
    admin.add_view(ModelView(Product, db.session))
    admin.add_view(ModelView(Order, db.session))

    stripe.api_key = app.config['STRIPE_SECRET_KEY']

    return app
