create table alunos (
    id integer primary key,
    nome text not null
);

create table cursos (
    id integer primary key,
    titulo text not NULL
);

create table alunos_cursos(
    id_aluno integer,
    ida_curso integer,
    foreign key (id_aluno) references alunos(id),
    foreign key (id_curso) references cursos(id)
);
create table curos(
    id integer primary key,
    titulo tex not null
);

create table alunos_cursos(
    id_alunos integer,
    id_curso integer,
    foreign key (id_aluno) references alunos(id)
    Foreign Key (id_curso) references cursos(id)
);
insert into cursos(titulo) values ('backend'), ('frontend')

select * from cursos;


