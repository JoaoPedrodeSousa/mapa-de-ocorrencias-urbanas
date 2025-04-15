import requests

from shapely import Point
from shapely.geometry import shape
from datetime import datetime

from src.errors.OutsideDistritoFederalError import OutsideDistritoFederalError

from src.entities.Occurrence import Occurrence
from src.repositories.OccurrenceRepository import OccurrenceRepository

class OccurrenceService():
    def __init__(self, occurrenceRepository:OccurrenceRepository):
        self._occurrence_repository = occurrenceRepository

    def save(self, category_id, description, coordinates) -> dict:
        try:
            x = coordinates[0]
            y = coordinates[1]

            geom = Point(x,y)
            
            self.isValidGeom(geom)

            occurrence = Occurrence(
                id = None,
                category_id = category_id,
                description = description,
                date = datetime.now(),
                geom = geom
            )

            self._occurrence_repository.save(occurrence = occurrence)
        
            features = self._make_feature(occurrence)
            geojson = self._make_geojson([features])

            return geojson
        
        except Exception as e:
            raise OutsideDistritoFederalError()

    def find(self, id) -> Occurrence:
        occurrence = self._occurrence_repository.find(id=id)
        features = self._make_feature(occurrence)
        geojson = self._make_geojson([features])

        return geojson

    def findAll(self) -> list:
        occurrences = self._occurrence_repository.findAll()

        features = [
            self._make_feature(occurrence) 
            for occurrence in occurrences
        ]
        
        geojson = self._make_geojson(features)
        return geojson
    
    def _make_feature(self, occurrence:Occurrence):
        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [occurrence.geom.x, occurrence.geom.y]},
            "properties": {
                "id": occurrence.id,
                "category_id": occurrence.category_id,
                "description": occurrence.description,
                "date": occurrence.date.isoformat()
            }
        }
    
    def _make_geojson(self, features:list) -> dict:
        return {
        "type": "FeatureCollection",
        "features": [feature for feature in features]
    }

    def isValidGeom(self, point:Point):
        wfs_df = requests.get("http://geoserver:8080/geoserver/limites_df/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=limites_df:limites_df&maxFeatures=50&outputFormat=application/json")

        geojson = wfs_df.json()
        feature = geojson["features"][0]["geometry"]

        geom_df = shape(feature)

        if geom_df.contains(point):
            return True
        
        raise Exception
        
