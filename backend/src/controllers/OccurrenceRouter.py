from flask import request, jsonify, make_response

from src.errors.OutsideDistritoFederalError import OutsideDistritoFederalError

from src.serializer.SerializerOccurrence import serializerOccurrence
from src.infrastructure.server import server
from src.entities.Occurrence import Occurrence
from src.services.OccurrenceService import OccurrenceService

from src.repositories.impl.OccurrenceSQLAlchemy import OccurrenceSQLAlchemy
from src.repositories.impl.CategorySQLAlchemy import CategorySQLAlchemy

app = server.get_app()

repository_occurrence = OccurrenceSQLAlchemy()
repository_category = CategorySQLAlchemy()
occurrence_service = OccurrenceService(repository_occurrence, repository_category)

@app.route("/occurrence", methods = ["POST"])
def create_occurrence():
    data:dict = request.json

    category_id = data.get('category')
    date = data.get('datetime')
    description = data.get('description')
    coordinates = data.get('geometry')

    try:
        occurrence = occurrence_service.save(category_id, date, description, coordinates)

        geojson = serializerOccurrence.to_geojson([occurrence])
        return make_response(jsonify(geojson),201)

    except KeyError as e :
        return make_response(jsonify({
            "error": "Elemento faltando na requisição. " + str(e),
        }),400)
    
    except OutsideDistritoFederalError as e:
        return make_response(jsonify({
            "error": str(e),
        }),400)

@app.route("/occurrence/<int:id>", methods = ["GET"])
def find_occurrence(id):
    occurrence = occurrence_service.find(id=id)
    geojson = serializerOccurrence.to_geojson([occurrence])
    return make_response(jsonify(geojson),200)

@app.route("/occurrence", methods = ["GET"])
def find_all_occurrences():

    occurrences = occurrence_service.findAll()

    geojson = serializerOccurrence.to_geojson(occurrences)

    return make_response(jsonify(geojson),200)
