import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    TESTING = True
