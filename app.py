from src.infrastructure.server import server
from src.infrastructure.database.database import connection

if __name__ == "__main__":
    db = connection.get_db()
    migrate = connection.get_migrate()
    
    server.init_server()
