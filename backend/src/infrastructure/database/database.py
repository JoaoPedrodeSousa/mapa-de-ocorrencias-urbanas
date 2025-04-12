from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from ..server import server

app = server.get_app()

class ConnectionPostGIS():
    def __init__(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/brasilia_df'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self._db:SQLAlchemy = SQLAlchemy(app)
        self._migrate:Migrate = Migrate(app,self._db)

    def get_db(self) -> SQLAlchemy:
        return self._db

    def get_migrate(self) -> Migrate:
        return self._migrate
    
connection = ConnectionPostGIS()