from datetime import datetime
from src.entities.Occurrence import Occurrence

class SerializerOccurrence():
    def to_geojson(self, occurrences:list) -> dict:
        features = [
            self._format_feature(occurrence) 
            for occurrence in occurrences
        ]
        return self._format_geojson(features)

    def _format_feature(self, occurrence:Occurrence) -> dict:
        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [occurrence.geom.x, occurrence.geom.y]},
            "properties": {
                "id": occurrence.id,
                "category_id": occurrence.category_id,
                "description": occurrence.description,
                "date": self._format_date(str(occurrence.date))
            }
        }
    
    def _format_geojson(self, features:list) -> dict:
        return {
        "type": "FeatureCollection",
        "features": features
    }

    def _format_date(self, date) -> str:
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
            except ValueError:
                try:
                    date = datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    return date
        return date.strftime("%d/%m/%Y")

serializerOccurrence = SerializerOccurrence()