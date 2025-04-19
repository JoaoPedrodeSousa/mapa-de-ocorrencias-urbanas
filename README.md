# Sistema de Cadastro de Ocorrências Georreferenciadas

## Visão Geral do Projeto

### Descrição do Propósito

Este sistema permite o **cadastro, visualização e análise de ocorrências georreferenciadas** entro dos limites do **Distrito Federal (DF)**.

### Público-Alvo e Casos de Uso

- **Órgãos públicos** e **prefeituras** que desejam monitorar ocorrências por localização.
- **Usuários cidadãos** para registrar denúncias, solicitações ou ocorrências.
- **Analistas** que trabalham com dados espaciais.

---

## Tecnologias Utilizadas

| Componente | Descrição |
|-----------|-----------|
| **Flask** | API REST back-end |
| **Vue.js** | Front-end |
| **Leaflet** | Biblioteca para mapas interativos |
| **PostgreSQL + PostGIS** | Banco de dados relacional com suporte espacial |
| **GeoServer** | Servidor de dados geoespaciais (WMS/WFS) |
| **Docker Compose** | Orquestração de containers |

## Instalação e Configuração

### Pré-Requisitos

- Docker
- Docker Compose

### Clonando o Projeto

``` bash
git clone https://github.com/JoaoPedrodeSousa/mapa-de-ocorrencias-urbanas.git
cd mapa-de-ocorrencias-urbanas
```

### Subindo o Sistema
No diretório ./mapa-de-ocorrencias-urbanas
``` bash
docker-compose up
docker exec -it geoserver bash
/publish_layers.sh
```
**obs.:** As camadas são publicadas automaticamente após a execução de `/publish_layers.sh`.


### Inicialização do Banco

O banco é iniciado automaticamente após o comando `docker-compose up` e fica disponível na porta `5432`.

### Variáveis de Ambiente

```bash
POSTGRES_DB = brasilia_df
POSTGRES_USER = postgres
POSTGRES_PASSWORD = postgres
DB_HOST = POSTGIS
GEOSERVER_ADMIN_USER = geoserver
GEOSERVER_ADMIN_PASSWORD = geoserver
```
---

## APIs REST

``` plaintext
http://localhost:5000/
```

### Endpoints

| Método | Rota               | Descrição                  |
|--------|--------------------|----------------------------|
| POST   | /occurrence       | Criar uma nova ocorrência.  |
| GET    | /occurrence       | Listar todas ocorrências.              |
| GET    | /occurrence/:id   | Obter detalhes de uma ocorrência específica.             |
| GET    | /category/:id   | Obter detalhes de uma categoria específica.             |
| GET    | /category   | Listar todas as categorias.             |

### Exemplo de Requisição

#### POST /occurence

```json
{
	"category":"1",
	"datetime": "2023-06-12",
	"description":"Teste Geometria",
	"geometry": [-47.729075, -15.736745]
}
```
#### Response

```json
{
  "type": "FeatureCollection",
  "features": [
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-47.729075, -15.736745]
    },
    "properties": {
      "id": 1,
      "category_id": 1,
      "description": "Teste Geometria",
      "date": "2023-06-12"
    }
  ]
}
```

### Validações

- Verificação se ponto (`lat/lon`) está **dentro dos limites do DF**.
- Categoria obrigatória.
- Data obrigatória.
- Descrição obrigatória.

---

## Front-End (Vue + Leaflet)
``` plaintext
http://localhost:5173/
```
### Funcionalidades

- Mapa interativo com Leaflet.
- Formulário de cadastro vinculado ao clique no mapa.
- Exibição das ocorrências com marcadores e legenda.
---

## GeoServer
``` plaintext
http://localhost:8082/
```
### Configuração

- Os dados são publicados após a execução de `publish_layers.sh` na fase de inicialização do sistema.
- Publicar camada `limites_Distrito federal` no formato **WMS/WFS**.
- Publicar camada `ocorrências` no formato **WFS**.

### Uso na API

O Geoserver é usado para publicação e consumo de dados geoespaciais:

- Limites do Distrito Federal: Uso em WMS para exibição no mapa da aplicação e WFS para validação da geometria inserida.
- Ocorrências: Uso de WFS para envio e manipulação de dado.

---

## Informações complementares
- As respostas dos Endpoints da API do Flask sempre retornam dados em formato [GeoJSON](https://geojson.org/). Apesar de não ser o formato de entrada de dados da API, é o formato de saída para todos os endpoints. 

- O mapeamento de portas do Geoserver foi feito como 8082:8080. Isso significa que caso queira acessar o Geoserver em seu navegador, então usar a porta `8082`, caso o Geoserver seja usado internamente pela própria aplicação, então usar a porta `8080`.

- Os dados inseridos estão no SRID WGS 84 - EPSG:4326 e são exibidos em WGS 84 - EPSG:3857. Isso é uma feature do Leaflet, não um bug. O CRS de exibição do mapa é diferente do CRS de dados do mapa.

