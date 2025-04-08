from src.errors.OutsideDistritoFederalError import OutsideDistritoFederalError

from shapely import Point
from geoalchemy2.shape import from_shape
from datetime import datetime

from src.entities.Occurrence import Occurence
from src.repositories.OccurrenceRepository import OccurenceRepository

class OccurrenceService():
    def __init__(self, occurenceRepository:OccurenceRepository):
        self._occurence_repository = occurenceRepository

    def save(self, category_id, description, coordinates) -> dict:
        x = coordinates[0]
        y = coordinates[1]

        occurence = Occurence(
            id = None,
            category_id = category_id,
            description = description,
            date = datetime.now(),
            geom = Point(x,y)
        )
        try:
            self._occurence_repository.save(occurence = occurence)
        except Exception as e:
            raise OutsideDistritoFederalError()
        features = self._make_feature(occurence)
        geojson = self._make_geojson([features])

        return geojson

    def find(self, id) -> Occurence:
        occurence = self._occurence_repository.find(id=id)
        features = self._make_feature(occurence)
        geojson = self._make_geojson([features])

        return geojson

    def findAll(self) -> list:
        ocurrences = self._occurence_repository.findAll()

        features = [
            self._make_feature(occurence) 
            for occurence in ocurrences
        ]
        
        geojson = self._make_geojson(features)
        return geojson
    
    def _make_feature(self, occurence:Occurence):
        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [occurence.geom.x, occurence.geom.y]},
            "properties": {
                "id": occurence.id,
                "category_id": occurence.category_id,
                "description": occurence.description,
                "date": occurence.date.isoformat()
            }
        }
    
    def _make_geojson(self, features:list) -> dict:
        return {
        "type": "FeatureCollection",
        "features": [feature for feature in features]
    }