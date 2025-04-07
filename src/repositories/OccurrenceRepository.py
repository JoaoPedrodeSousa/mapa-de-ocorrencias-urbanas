from src.entities.Occurrence import Occurence
from abc import ABC, abstractmethod

class OccurenceRepository(ABC):
    @abstractmethod
    def save(self) -> None: ...
    
    @abstractmethod
    def find(self) -> Occurence: ...
    
    @abstractmethod
    def findAll(self) -> list: ...
