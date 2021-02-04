import os


class Config(object):
    SECRET_KEY = os.urandom(24)
    APP_STATE = os.environ.get("APP_STATE")  # production, development, debug, shutdown


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    APP_STATE = os.environ.get("TESTING_APP_STATE")


class DevConfig(Config):
    TEMPLATES_AUTO_RELOAD = True
    APP_STATE = os.environ.get("LOCAL_APP_STATE")


class ProdConfig(Config):
    pass


configs = {
    "development": DevConfig,
    "test": TestConfig,
    "production": ProdConfig,
    "default": ProdConfig,
}
