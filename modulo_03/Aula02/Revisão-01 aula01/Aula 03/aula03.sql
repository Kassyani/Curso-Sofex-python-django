-- Active: 1759940571146@@127.0.0.1@3306
create table professores 
( id integer primary key, 
nome text not null
);

create table alunos ( 
    id integer primary key, 
    nome text not null,
    id_professor integer,
foreign key(id_professor) references professores(id));

drop table alunos;

insert into professores(nome) values ('Anderson'),('Paulo');
select * from professores;

insert into alunos(nome, id_professor) values ('Pedro',1),('Maria',2),('José',1);

select * from alunos;

select id as identificador, nome, id_professor as registro_professor from alunos;

select alunos.nome as nome_aluno, professores.nome as nome_professor from alunos
inner join professores on alunos.id_professor = professores.id;