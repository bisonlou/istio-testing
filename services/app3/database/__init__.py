import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db_user = os.getenv('DATABASE_USER', None)
db_pass = os.getenv('DATABASE_PASSWORD', None)
db_host = os.getenv('DATABASE_HOST', None)
db_name = os.getenv('DATABASE_NAME', None)

database_uri = f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'
db = SQLAlchemy()

def create_db(app, database_uri=database_uri):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db = SQLAlchemy(app)
    db.app = app
    db.init_app(app)

    import models.hit

    db.create_all()
    Migrate(app, db)

