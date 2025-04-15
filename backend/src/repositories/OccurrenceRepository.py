from src.entities.Occurrence import Occurrence
from abc import ABC, abstractmethod

class OccurrenceRepository(ABC):
    @abstractmethod
    def save(self, occurrence:Occurrence) -> None: ...
    
    @abstractmethod
    def find(self, id:id) -> Occurrence: ...
    
    @abstractmethod
    def findAll(self) -> list: ...
