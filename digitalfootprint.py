import os

from app import create_app


env = os.environ.get("FLASK_ENV", "default")
application = create_app(config_name=env)
