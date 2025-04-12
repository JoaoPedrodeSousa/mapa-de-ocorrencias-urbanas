from geoalchemy2.shape import from_shape, to_shape

from src.infrastructure.database.database import connection
from src.entities.Occurrence import Occurence
from src.infrastructure.database.models import OccurrenceModel
from ..OccurrenceRepository import OccurenceRepository

class OccurenceSQLAlchemy(OccurenceRepository):
    def __init__(self):
        self._db = connection.get_db()
    
    def save(self, occurence:Occurence):
        model = OccurrenceModel(
            id=None,
            categoria_id= occurence.category_id,
            data_registro = occurence.date,
            descricao = occurence.description,
            geom = from_shape(occurence.geom)
        )

        self._db.session.add(model)
        self._db.session.commit()
        occurence.id = model.id

    def find(self, id:int):
        model = OccurrenceModel.query.filter_by(id=id).first_or_404() 
        occurence = Occurence(
            id= model.id,
            category_id= model.categoria_id,
            description = model.descricao,
            date = model.data_registro,
            geom = to_shape(model.geom)
        )
        return occurence

    def findByCategory(self, category_id:int):
        models = OccurrenceModel.query.filter_by(categoria_id = category_id).all()

        occurences = [ Occurence(
            id= model.id,
            category_id= model.categoria_id,
            description = model.descricao,
            date = model.data_registro,
            geom = to_shape(model.geom)
        )for model in models]

        return occurences
    
    def findAll(self):
        models = OccurrenceModel.query.all() 

        occurences = [ Occurence(
            id= model.id,
            category_id= model.categoria_id,
            description = model.descricao,
            date = model.data_registro,
            geom = to_shape(model.geom)
        )for model in models]
        
        return occurences