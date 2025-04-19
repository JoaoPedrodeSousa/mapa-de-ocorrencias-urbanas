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

    def find(self, id) -> Occurrence:
        return self._occurrence_repository.find(id=id)

    def save(self, category_id, date, description, coordinates) -> dict:
        x = coordinates[0]
        y = coordinates[1]
        
        geom = Point(x,y)

        try:
            self.is_valid_geometry(geom)
            occurrence = Occurrence(
                id = None,
                category_id = category_id,
                description = description,
                date = date,
                geom = geom
            )
            self._occurrence_repository.save(occurrence = occurrence)
            return occurrence
        
        except Exception as e:
            raise OutsideDistritoFederalError()

    def findAll(self) -> list:
        wfs_occurrences = requests.get("http://geoserver:8080/geoserver/ocorrencias_wks/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=ocorrencias_wks:ocorrencias&maxFeatures=50&outputFormat=application/json")

        wfs_occurrences = wfs_occurrences.json()
        occurrences = []
        features = wfs_occurrences["features"]
        for feature in features:
            x = feature["geometry"]["coordinates"][0]
            y = feature["geometry"]["coordinates"][1]
            
            properties = feature["properties"]
            occurence = Occurrence(
                id = int(feature["id"].split(".")[1]),
                category_id = properties["categoria_id"],
                date = properties['data_registro'],
                description = properties['descricao'],
                geom = Point(x,y)
            )
            occurrences.append(occurence)

        return occurrences

    def is_valid_geometry(self, point:Point):
        wfs_df = requests.get("http://geoserver:8080/geoserver/ocorrencias_wks/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=ocorrencias_wks:limite_do_distrito_federal&maxFeatures=50&outputFormat=application/json")

        geojson = wfs_df.json()
        feature = geojson["features"][0]["geometry"]

        geom_df = shape(feature)

        if geom_df.contains(point):
            return True
        
        raise Exception
        
