from flask import Flask
from flask_cors import CORS

class Server():
    def __init__(self):
        self._app = Flask(__name__)
        CORS(self._app)

    def init_server(self) -> None:
        self._app.run(debug=True)
    
    def get_app(self) -> Flask:
        return self._app
    
server = Server()