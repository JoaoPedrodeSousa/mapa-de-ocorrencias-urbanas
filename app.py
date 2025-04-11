from backend.src.infrastructure.server import server
from backend.src.infrastructure.database.database import connection
from backend.src.infrastructure.database.models import *
from backend.src.controllers.OccurenceRouter import *

app = server.get_app()

if __name__ == "__main__":
    db = connection.get_db()
    migrate = connection.get_migrate()

    server.init_server()
