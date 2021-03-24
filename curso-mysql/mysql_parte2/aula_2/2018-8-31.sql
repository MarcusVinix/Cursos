use sql2;

select * from aluno;

select * from aluno limit 0, 3;

select * from aluno where nome like 'João%' limit 0, 5;

select * from aluno where nome like '%João%' limit 0, 3;

select * from aluno limit 0, 2;

select * from aluno where email like '%.com' limit 0, 3;

select * from aluno where email like '%.com' order by nome limit 0,2;

