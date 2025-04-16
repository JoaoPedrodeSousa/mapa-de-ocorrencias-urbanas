import requests

from shapely import Point
from shapely.geometry import shape
from src.errors.OutsideDistritoFederalError import OutsideDistritoFederalError
from datetime import datetime

from src.entities.Occurrence import Occurrence
from src.repositories.OccurrenceRepository import OccurrenceRepository
from src.repositories.CategoryRepository import CategoryRepository

class OccurrenceService():
    def __init__(self, occurrenceRepository:OccurrenceRepository, categoryRepository:CategoryRepository):
        self._occurrence_repository = occurrenceRepository
        self._category_repository = categoryRepository

    def save(self, category_id, date, description, coordinates) -> dict:
        x = coordinates[0]
        y = coordinates[1]
        
        geom = Point(x,y)

        date_obj = datetime.strptime(date, "%Y-%m-%d")
        dateformatter = date_obj.strftime("%Y-%m-%d")

        try:
            self.isValidGeom(geom)
        except Exception as e:
            raise OutsideDistritoFederalError()

        occurrence = Occurrence(
            id = None,
            category_id = category_id,
            description = description,
            date = dateformatter,
            geom = geom
        )

        self._occurrence_repository.save(occurrence = occurrence)
    
        features = self._make_feature(occurrence)
        geojson = self._make_geojson([features])

        return geojson
        

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
    
    def findAllWithGeoserver(self) -> list:
        wfs_occurrences = requests.get("http://geoserver:8080/geoserver/limites_df/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=limites_df%3Aocorrencias&maxFeatures=50&outputFormat=application/json") #lista de geojson

        wfs_occurrences = wfs_occurrences.json()
        categories_hashmap = self._make_hashmap()

        features = wfs_occurrences["features"]
        for feature in features:
            
            properties:dict = feature["properties"]
            categoria_id = properties["categoria_id"]
            
            properties["id"] = int(feature["id"][-1])
            properties["categoria"] = categories_hashmap[categoria_id]

            feature.pop("bbox",None)
            feature.pop("geometry_name",None)
            feature.pop("id",None)

        geojson = self._make_geojson(features)
        return geojson

    def _make_hashmap(self):
        categories = self._category_repository.findAll()

        categories_hashmap = {}

        for category in categories:
            categories_hashmap[category.id] = category.name

        return categories_hashmap

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
                "date": occurrence.date
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
        
