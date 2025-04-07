from src.entities.Category import Category
from abc import ABC, abstractmethod

class CategoryRepository(ABC):
    
    @abstractmethod
    def find(self) -> Category: ...
    
    @abstractmethod
    def findAll(self) -> list: ...