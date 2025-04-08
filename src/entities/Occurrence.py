from dataclasses import dataclass
from shapely import Point
from datetime import datetime

@dataclass
class Occurence():
    id: int | None
    category_id: int
    description: str
    date: datetime
    geom: Point
