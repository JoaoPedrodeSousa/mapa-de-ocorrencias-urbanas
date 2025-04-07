from src.repositories.CategoryRepository import CategoryRepository

class CategoryService():
    def __init__(self, categoryRepository:CategoryRepository):
        self._category_repository = categoryRepository

    def findAll(self):
        categories = self._category_repository.findAll()
        return categories
    
    def find(self, name):
        category = self._category_repository.findAll(name)
        return category