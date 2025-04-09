import requests

from shapely import Point
from shapely.geometry import shape
from datetime import datetime

from src.errors.OutsideDistritoFederalError import OutsideDistritoFederalError

from src.entities.Occurrence import Occurence
from src.repositories.OccurrenceRepository import OccurenceRepository

class OccurrenceService():
    def __init__(self, occurenceRepository:OccurenceRepository):
        self._occurence_repository = occurenceRepository

    def save(self, category_id, description, coordinates) -> dict:
        try:
            x = coordinates[0]
            y = coordinates[1]

            geom = Point(x,y)
            
            self.isValidGeom(geom)

            occurence = Occurence(
                id = None,
                category_id = category_id,
                description = description,
                date = datetime.now(),
                geom = geom
            )

            self._occurence_repository.save(occurence = occurence)
        
            features = self._make_feature(occurence)
            geojson = self._make_geojson([features])

            return geojson
        
        except Exception as e:
            raise OutsideDistritoFederalError()

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

    def isValidGeom(self, point:Point):
        wfs_df = requests.get("http://localhost:8082/geoserver/limites_df/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=limites_df:tb_limites_df&maxFeatures=50&outputFormat=application/json")

        geojson = wfs_df.json()
        feature = geojson["features"][0]["geometry"]

        geom_df = shape(feature)

        if geom_df.contains(point):
            return True
        
        raise Exception
        
