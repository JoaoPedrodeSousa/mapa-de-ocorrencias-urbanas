from shapely import Point

class Occurence():
    id: int | None
    categoria_id: int
    descricao: str
    geom: Point
