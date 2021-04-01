from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from turbo_flask import Turbo

from faker import Faker

fake = Faker("cs_CZ")

db = SQLAlchemy(session_options={"autoflush": False, "autocommit": False})
migrate = Migrate()
turbo = Turbo()


def create_app(config_name="default"):
    application = Flask(__name__, instance_relative_config=True)

    # CONFIG
    from config import configs

    application.config.from_object(configs[config_name])

    # APPS
    db.init_app(application)
    migrate.init_app(application, db)
    turbo.init_app(application)

    # CONTROLLERS
    from .controllers import register_all_controllers  # noqa: F401

    register_all_controllers(application)

    from .controllers import register_error_handlers  # noqa: F401

    register_error_handlers(application)

    # MODULES

    # from .auth import create_module as auth_create_module

    # auth_create_module(application)

    return application
