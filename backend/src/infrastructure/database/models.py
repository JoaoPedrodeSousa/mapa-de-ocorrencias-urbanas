from geoalchemy2 import Geometry

from .database import connection

db = connection.get_db()

class CategoryModel(db.Model):
    __tablename__ = 'categoria'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30),nullable=False)

class OccurrenceModel(db.Model):
  __tablename__ = 'ocorrencias'

  id = db.Column(db.Integer, primary_key = True)
  categoria_id = db.Column(db.SmallInteger, db.ForeignKey('categoria.id'), nullable = False)
  descricao = db.Column(db.String(125))
  data_registro = db.Column(db.DateTime(timezone=False),nullable = False)
  geom = db.Column(Geometry(geometry_type='POINT', srid=4326, spatial_index=True))

  dom_categoria = db.relationship(
    'CategoryModel',
    backref='dom_categoria',
    foreign_keys=[categoria_id]
  )