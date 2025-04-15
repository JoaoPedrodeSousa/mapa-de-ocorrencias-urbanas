from geoalchemy2.shape import from_shape, to_shape

from src.infrastructure.database.database import connection
from src.entities.Occurrence import Occurrence
from src.infrastructure.database.models import OccurrenceModel
from ..OccurrenceRepository import OccurrenceRepository

class OccurrenceSQLAlchemy(OccurrenceRepository):
    def __init__(self):
        self._db = connection.get_db()
    
    def save(self, occurrence:Occurrence):
        model = OccurrenceModel(
            id=None,
            categoria_id= occurrence.category_id,
            data_registro = occurrence.date,
            descricao = occurrence.description,
            geom = from_shape(occurrence.geom)
        )

        self._db.session.add(model)
        self._db.session.commit()
        occurrence.id = model.id

    def find(self, id:int):
        model = OccurrenceModel.query.filter_by(id=id).first_or_404() 
        occurrence = Occurrence(
            id= model.id,
            category_id= model.categoria_id,
            description = model.descricao,
            date = model.data_registro,
            geom = to_shape(model.geom)
        )
        return occurrence

    def findByCategory(self, category_id:int):
        models = OccurrenceModel.query.filter_by(categoria_id = category_id).all()

        occurrences = [ Occurrence(
            id= model.id,
            category_id= model.categoria_id,
            description = model.descricao,
            date = model.data_registro,
            geom = to_shape(model.geom)
        )for model in models]

        return occurrences
    
    def findAll(self):
        models = OccurrenceModel.query.all() 

        occurrences = [ Occurrence(
            id= model.id,
            category_id= model.categoria_id,
            description = model.descricao,
            date = model.data_registro,
            geom = to_shape(model.geom)
        )for model in models]
        
        return occurrences