import os
from pathlib import Path
basedir = Path(__file__).parent.absolute()

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'rsrs_treasure_map'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                            'sqlite:///' + str(basedir / 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
