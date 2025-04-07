from shapely import Point
from geoalchemy2.shape import from_shape

from src.entities.Occurrence import Occurence

from src.repositories.OccurrenceRepository import OccurenceRepository
from src.repositories.CategoryRepository import CategoryRepository

class OccurrenceService():
    def __init__(self, categoryRepository:CategoryRepository, occurenceRepository:OccurenceRepository):
        self._category_repository = categoryRepository
        self._occurence_repository = occurenceRepository

    def save(self, category_id, description, coordenates) -> Occurence:
        x = coordenates[0]
        y = coordenates[1]

        occurence = Occurence(
            id = None,
            category_id = category_id,
            description = description,
            geom = from_shape(Point(x,y))
        )

        self._occurence_repository.save(occurence = occurence)
        return occurence

    def find(self, id) -> Occurence:
        occurence = self._occurence_repository.find(id=id)
        return occurence

    def findAll(self) -> list:
        ocurrences = self._occurence_repository.findAll()
        return ocurrences