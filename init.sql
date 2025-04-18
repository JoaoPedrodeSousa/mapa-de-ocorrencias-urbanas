CREATE DATABASE brasilia_df;

\c brasilia_df;

CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS brasilia_df.public.categoria
(
    id serial,
    nome character varying(30) NOT NULL,
    CONSTRAINT categoria_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS brasilia_df.public.limites_df
(
    id serial,
    geom geometry(MultiPolygon,4326),
    CONSTRAINT limites_df_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS brasilia_df.public.ocorrencias
(
    id serial,
    categoria_id smallint NOT NULL,
    descricao character varying(125),
    data_registro timestamp without time zone NOT NULL,
    geom geometry(Point,4326),
    CONSTRAINT ocorrencias_pkey PRIMARY KEY (id),
    CONSTRAINT ocorrencias_categoria_id_fkey FOREIGN KEY (categoria_id)
        REFERENCES brasilia_df.public.categoria (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE INDEX IF NOT EXISTS idx_ocorrencias_geom
    ON public.ocorrencias USING gist
    (geom)
    TABLESPACE pg_default;

INSERT INTO categoria(nome) VALUES('CONCENTRAÇÃO DE LIXO');
INSERT INTO categoria(nome) VALUES('RUA COM BURACO');
INSERT INTO categoria(nome) VALUES('CASA COM FANTASMAS');
INSERT INTO categoria(nome) VALUES('FOCO DE DENGUE');
INSERT INTO categoria(nome) VALUES('PROBLEMAS COM ILUMINAÇÃO');
INSERT INTO categoria(nome) VALUES('TRANSITO CONGESTIONADO');
INSERT INTO categoria(nome) VALUES('ACIDENTE DE CARRO');
INSERT INTO categoria(nome) VALUES('EVENTO CULTURAL');
INSERT INTO categoria(nome) VALUES('FEIRA DO LIVRO');
