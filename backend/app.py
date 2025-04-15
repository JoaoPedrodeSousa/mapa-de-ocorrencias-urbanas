from src.infrastructure.server import server
from src.infrastructure.database.database import connection
from src.infrastructure.database.models import *
from src.controllers.OccurrenceRouter import *
from src.controllers.CategoryRouter import *

app = server.get_app()

if __name__ == "__main__":
    db = connection.get_db()
    migrate = connection.get_migrate()
    server.init_server()
