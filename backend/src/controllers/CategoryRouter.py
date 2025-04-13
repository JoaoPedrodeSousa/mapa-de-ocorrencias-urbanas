from flask import jsonify, make_response

from src.infrastructure.server import server
from src.entities.Category import Category

from src.services.CategoryService import CategoryService

from src.repositories.impl.CategorySQLAlchemy import CategorySQLAlchemy

app = server.get_app()
repository = CategorySQLAlchemy()

@app.route("/category", methods=["GET"])
def findAll():
    service = CategoryService(repository)
    categories = service.findAll()
    return make_response(jsonify(categories),200)