from src.infrastructure.server import server
from src.infrastructure.database.database import connection
from src.infrastructure.database.models import *
from src.controllers.OccurenceRouter import *
from src.controllers.CategoryRouter import *

from flask_cors import CORS
app = server.get_app()
if __name__ == "__main__":
    db = connection.get_db()
    migrate = connection.get_migrate()
    server.init_server()
