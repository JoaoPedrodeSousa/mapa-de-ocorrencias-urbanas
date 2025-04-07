from shapely import Point

class Occurence():
    id: int | None
    category_id: int
    description: str
    geom: Point
