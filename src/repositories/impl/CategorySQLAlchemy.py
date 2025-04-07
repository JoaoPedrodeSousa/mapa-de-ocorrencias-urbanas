from src.infrastructure.database.database import connection
from src.entities.Category import Category
from src.infrastructure.database.models import CategoryModel
from ..CategoryRepository import CategoryRepository

class CategorySQLAlchemy(CategoryRepository):
    def __init__(self):
        self._db = connection.get_db()
    
    def find(self, id) -> Category:
        model = CategoryModel.query.filter_by(id=id).first_or_404()

        return Category(
            id = model.id,
            name = model.nome
        )

    def findAll(self) -> list:

        models = CategoryModel.query.all()

        categories = [ Category(
            id = model.id,
            name = model.nome
        ) for model in models]

        return categories