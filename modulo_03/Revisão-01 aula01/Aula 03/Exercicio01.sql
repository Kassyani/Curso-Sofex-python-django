-- Active: 1759940571146@@127.0.0.1@3306
CREATE TABLE autores(
    id_autor INTEGER PRIMARY KEY,
    nome TEXT,
    nacionalidade TEXT
);

CREATE TABLE livros(
    id_livro INTEGER PRIMARY KEY,
    ano_publicaçao NULL,
    titulo TEXT,
    id_autor INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autores(id)
)