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

INSERT INTO categoria(nome) VALUES('Concentração de lixo');
INSERT INTO categoria(nome) VALUES('Rua com buraco');
INSERT INTO categoria(nome) VALUES('Casa com fantasmas');
INSERT INTO categoria(nome) VALUES('Foco de Dengue');
INSERT INTO categoria(nome) VALUES('Problemas com iluminação');
INSERT INTO categoria(nome) VALUES('Transito Congestionado');
INSERT INTO categoria(nome) VALUES('Acidente de carro');
INSERT INTO categoria(nome) VALUES('Evento cultural');
INSERT INTO categoria(nome) VALUES('Feira do livro');
