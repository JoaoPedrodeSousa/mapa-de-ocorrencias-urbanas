#!/bin/bash

GEOSERVER_URL="http://geoserver:8080/geoserver"
USER="geoserver"
PASS="geoserver"

WORKSPACE="ocorrencias_wks"

POSTGIS_DATASTORE="brasilia_df"
LAYER_OCCURRENCES="ocorrencias"

SHAPEFILE_DATASTORE="limites"
LAYER_SHAPEFILE="/shapefile/limites_df.zip"

STYLE_SHAPEFILE_DF="limite_do_distrito_federal"
SLD_PATH="/shapefile/estilo_df.sld"

until curl -u "$USER:$PASS" -s "$GEOSERVER_URL/rest/workspaces" > /dev/null; do
  echo "Aguardando o GeoServer estar pronto..."
  sleep 15
done

echo "Criando workspace: $WORKSPACE"
curl -u $USER:$PASS -XPOST -H "Content-type: text/xml" \
     -d "<workspace><name>${WORKSPACE}</name></workspace>" \
     "$GEOSERVER_URL/rest/workspaces"

echo "Criando datastore PostGIS: $POSTGIS_DATASTORE"
curl -u $USER:$PASS -XPOST -H "Content-type: text/xml" \
     -d "<dataStore>
            <name>${POSTGIS_DATASTORE}</name>
            <connectionParameters>
              <host>postgis</host>
              <port>5432</port>
              <database>brasilia_df</database>
              <user>postgres</user>
              <passwd>postgres</passwd>
              <dbtype>postgis</dbtype>
            </connectionParameters>
         </dataStore>" \
     "$GEOSERVER_URL/rest/workspaces/${WORKSPACE}/datastores"

echo "Publicando camada: $LAYER_OCCURRENCES"
curl -u $USER:$PASS -XPOST -H "Content-type: text/xml" \
     -d "<featureType><name>${LAYER_OCCURRENCES}</name></featureType>" \
     "$GEOSERVER_URL/rest/workspaces/${WORKSPACE}/datastores/${POSTGIS_DATASTORE}/featuretypes"

echo "Publicando camada: $LAYER_SHAPEFILE"
curl -u $USER:$PASS -XPUT \
  -H "Content-type: application/zip" \
  --data-binary @"$LAYER_SHAPEFILE" \
  "$GEOSERVER_URL/rest/workspaces/${WORKSPACE}/datastores/${SHAPEFILE_DATASTORE}/file.shp"

echo "Criando estilo: $STYLE_SHAPEFILE_DF"
curl -u $USER:$PASS -XPOST -H "Content-type: text/xml" \
-d "<style>
      <name>${STYLE_SHAPEFILE_DF}</name>
      <filename>${STYLE_SHAPEFILE_DF}.sld</filename>
    </style>" \
"$GEOSERVER_URL/rest/workspaces/${WORKSPACE}/styles"

echo "Publicando estilo: $STYLE_SHAPEFILE_DF"
curl -u $USER:$PASS -XPUT -H "Content-type: application/vnd.ogc.sld+xml" \
--data-binary @"$SLD_PATH" \
"$GEOSERVER_URL/rest/workspaces/${WORKSPACE}/styles/${STYLE_SHAPEFILE_DF}"

echo "Aplicando estilo ${STYLE_SHAPEFILE_DF}"
curl -u $USER:$PASS -XPUT -H "Content-type: text/xml" \
-d "<layer><defaultStyle><name>${STYLE_SHAPEFILE_DF}</name></defaultStyle></layer>" \
"$GEOSERVER_URL/rest/layers/${WORKSPACE}:limite_do_distrito_federal"
