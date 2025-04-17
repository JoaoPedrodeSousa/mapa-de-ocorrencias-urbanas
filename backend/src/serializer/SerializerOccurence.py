from src.entities.Occurrence import Occurrence

class SerializerOccurence():
    def to_geojson(self, occurrences:list):
        features = [
            self._format_feature(occurrence) 
            for occurrence in occurrences
        ]
        return self._format_geojson(features)

    def wfs_to_geojson(self, wfs:dict, categories:dict):
        features = self._format_wfs(wfs,categories)
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
                "date": occurrence.date
            }
        }
    
    def _format_geojson(self, features:list) -> dict:
        return {
        "type": "FeatureCollection",
        "features": features
    }

    def _format_wfs(self, wfs:dict, categories:dict):
        features = wfs["features"]

        for feature in features:
            properties:dict = feature["properties"]
            categoria_id = properties["categoria_id"]
            
            properties["id"] = int(feature["id"][-1])
            properties["categoria"] = categories[categoria_id]

            feature.pop("bbox",None)
            feature.pop("geometry_name",None)
            feature.pop("id",None)
        
        return features


serializerOccurence = SerializerOccurence()