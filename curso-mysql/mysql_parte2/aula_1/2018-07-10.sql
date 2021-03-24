/*AUlA 1*/
create database sql2;

/*Adicionei a tabela dada pelo curso*/

use sql2;

show tables;

/*teste*/
select a.nome, c.nome from 
aluno a 
join matricula m on a.id = m.aluno_id 
join curso c on c.id = m.curso_id;

select a.nome from aluno a where exists 
(select m.id from matricula m where m.aluno_id = a.id);

select a.nome from aluno a where not exists 
(select m.id from matricula m where m.aluno_id = a.id);

select a.nome from aluno a where not exists 
(select m.id from matricula m where m.aluno_id = a.id 
and m.data > now() - interval 6 month);

/*Usando o EXISTS*/
select a.nome from aluno a where not exists (select m.id from matricula m where m.aluno_id = a.id);

/*Mais EXISTS*/
select a.nome from aluno a 
where 
not exists 
  (select m.id from matricula m 
   where m.aluno_id = a.id and m.data > now() - interval 45 day
  );

  /*fim*/