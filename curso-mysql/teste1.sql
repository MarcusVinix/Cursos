create table aluno
(id int NOT NULL auto_increment primary key, 
nome_aluno varchar(100) not null, 
idade varchar(50) not null, 
nascimento  varchar(100) not null, 
telefone varchar(15),
inicio varchar(20) not null,
professor_id int NOT NULL, 
turma_id int NOT NULL);

create table turma
(id int NOT NULL auto_increment primary key,
sala varchar(50) NOT NUll);
 

create table professor
(id int NOT NULL auto_increment primary key,
nome_professor varchar(100) NOT NULL);

alter table aluno add FOREIGN KEY (professor_id) references professor(id);
alter table aluno add FOREIGN KEY (turma_id) references turma(id);

INSERT INTO turma (sala) values ('SAT3');
INSERT INTO turma (sala) values ('SQ3');
INSERT INTO turma (sala) values ('SQ5');

INSERT INTO professor (nome_professor) values ('Samuel Justino');
INSERT INTO professor (nome_professor) values ('Maria Claudia');

INSERT INTO aluno (nome_aluno, idade, nascimento, telefone, inicio, professor_id, turma_id) VALUES
('Marcus Vinicius Nascimento De Souza', '17', '28/11/200', '(11) 94241-8283','03/12/2016', '2', '1');
INSERT INTO aluno (nome_aluno, idade, nascimento, telefone, inicio, professor_id, turma_id) VALUES
('Vitoria do Prado da Conceição', '16', '05/01/2002', '(11) 2467-9534','02/08/2017', '2', '3');
INSERT INTO aluno (nome_aluno, idade, nascimento, telefone, inicio, professor_id, turma_id) VALUES
('João Victor Sousa  de Moraes Ferreira', '17', '18/05/2001', '(11) 98387-0964','21/03/2017', '1', '2');
INSERT INTO aluno (nome_aluno, idade, nascimento, telefone, inicio, professor_id, turma_id) VALUES
('Kevyn Venancio Fidelis Silva', '19', '02/05/1999', '(11) 95834-5369','20/03/2016', '1', '2');
INSERT INTO aluno (nome_aluno, idade, nascimento, telefone, inicio, professor_id, turma_id) VALUES
('Vitor Silverio Puga', '16', '12/09/2001', '(11) 95022-9815','03/12/2016', '1', '1');

select turma.sala, professor.nome_professor, nome_aluno  from aluno
inner join professor on aluno.professor_id = professor.id 
inner join turma on aluno.turma_id = turma.id;



