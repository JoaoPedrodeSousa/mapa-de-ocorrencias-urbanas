import requests
import geopandas as gpd

class GeoserverService():
    def __init__(self):
        self.base_url = "http://localhost:8082/geoserver/rest"
    def create_datastore(self, workspace, name, host, port, database, user, password):
        url = f"{self.base_url}/workspaces/{workspace}/datastores"
        auth = ("geoserver", "geoserver")
        
        body = {
        "dataStore": {
            "name": name,
            "connectionParameters": {
                "entry": [{
                        "@key":"host",
                        "$":host
                    },{
                        "@key":"port",
                        "$":port
                    },{
                        "@key":"database",
                        "$":database
                    },{
                        "@key":"user",
                        "$": user
                    },{
                        "@key":"passwd",
                        "$":password
                    },{
                        "@key":"dbtype",
                        "$":"postgis"
                    }]
                }
            }
        }

        response = requests.post(url=url, auth=auth, json=body)
        return response
    
