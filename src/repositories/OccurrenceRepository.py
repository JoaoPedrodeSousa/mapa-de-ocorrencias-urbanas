from src.entities.Occurrence import Occurence
from abc import ABC, abstractmethod

class OccurenceRepository(ABC):
    @abstractmethod
    def save(self, occurence:Occurence) -> None: ...
    
    @abstractmethod
    def find(self, id:id) -> Occurence: ...
    
    @abstractmethod
    def findAll(self) -> list: ...
