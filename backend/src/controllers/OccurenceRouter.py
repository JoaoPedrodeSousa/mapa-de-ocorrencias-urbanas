from flask import request, jsonify, make_response

from backend.src.errors.OutsideDistritoFederalError import OutsideDistritoFederalError

from backend.src.infrastructure.server import server
from backend.src.entities.Occurrence import Occurence

from backend.src.services.OccurenceService import OccurrenceService
from backend.src.services.CategoryService import CategoryService

from backend.src.repositories.impl.OccurenceSQLAlchemy import OccurenceSQLAlchemy
from backend.src.repositories.impl.CategorySQLAlchemy import CategorySQLAlchemy

app = server.get_app()

category_repository = CategorySQLAlchemy()
occurence_repository = OccurenceSQLAlchemy()

@app.route("/occurence", methods = ["POST"])
def create_occurence():
    try:
        category_service = CategoryService(category_repository)
        data:dict = request.json

        category_name = data.get('category_name')
        category_id = category_service.find(category_name).id
        description = data.get('description')
        coordinates = data.get('geometry')

        occurrence_service = OccurrenceService(occurence_repository)
        geojson:dict = occurrence_service.save(category_id, description, coordinates)

    except KeyError as e :
        return make_response(jsonify({
            "error": "Elemento faltando na requisição. " + str(e),
        }),400)
    
    except OutsideDistritoFederalError as e:
        return make_response(jsonify({
            "error": str(e),
        }),400)
    
    return make_response(jsonify(geojson),201)


@app.route("/occurence/<int:id>", methods = ["GET"])
def find_occurence(id):
    occurrence_service = OccurrenceService(occurence_repository)
    geojson = occurrence_service.find(id=id)

    return make_response(jsonify(geojson),200)


@app.route("/occurence", methods = ["GET"])
def find_all_occurence():
    occurrence_service = OccurrenceService(occurence_repository)
    geojson = occurrence_service.findAll()

    return make_response(jsonify(geojson),200)