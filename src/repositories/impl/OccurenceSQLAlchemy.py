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
            categoria_id= occurence.categoria_id,
            descricao = occurence.descricao,
            geom = occurence.geom
        )

        self._db.session.add(model)
        self._db.session.commit()
        occurence.id = model.id
    
    def find(self, id:int):
        model = OccurrenceModel.query.filter_by(id=id).first_or_404() 
        occurence = Occurence(
            id= model.id,
            categoria_id= model.categoria_id,
            descricao = model.descricao,
            geom = model.geom
        )
        return occurence

    def findByCategory(self, categoria_id:int):
        models = OccurrenceModel.query.filter_by(categoria_id = categoria_id).all()

        occurences = [ Occurence(
            id= model.id,
            categoria_id= model.categoria_id,
            descricao = model.descricao,
            geom = model.geom
        )for model in models]

        return occurences
    
    def findAll(self):
        models = OccurrenceModel.query.all() 
        occurences = [ Occurence(
            id= model.id,
            categoria_id= model.categoria_id,
            descricao = model.descricao,
            geom = model.geom
        )for model in models]
        return occurences