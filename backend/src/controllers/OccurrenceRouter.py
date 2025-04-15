from flask import request, jsonify, make_response

from src.errors.OutsideDistritoFederalError import OutsideDistritoFederalError

from src.infrastructure.server import server
from src.entities.Occurrence import Occurrence

from src.services.OccurrenceService import OccurrenceService
from src.services.CategoryService import CategoryService

from src.repositories.impl.OccurrenceSQLAlchemy import OccurrenceSQLAlchemy
from src.repositories.impl.CategorySQLAlchemy import CategorySQLAlchemy

app = server.get_app()

category_repository = CategorySQLAlchemy()
occurrence_repository = OccurrenceSQLAlchemy()

@app.route("/occurrence", methods = ["POST"])
def create_occurrence():
    try:
        category_service = CategoryService(category_repository)
        data:dict = request.json
        print(data)

        category_name = data.get('category_name')
        category_id = category_service.find(category_name).id
        description = data.get('description')
        coordinates = data.get('geometry')

        occurrence_service = OccurrenceService(occurrence_repository)
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


@app.route("/occurrence/<int:id>", methods = ["GET"])
def find_occurrence(id):
    occurrence_service = OccurrenceService(occurrence_repository)
    geojson = occurrence_service.find(id=id)

    return make_response(jsonify(geojson),200)


@app.route("/occurrence", methods = ["GET"])
def find_all_occurrence():
    occurrence_service = OccurrenceService(occurrence_repository)
    geojson = occurrence_service.findAll()

    return make_response(jsonify(geojson),200)