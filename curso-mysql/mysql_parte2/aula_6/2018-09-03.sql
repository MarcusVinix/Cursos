use sql2

/*Média dos alunos*/
select a.nome, avg(n1.nota) as media, 
avg(n1.nota) - (select avg(n2.nota) from nota n2) as diferenca
from nota n1
join resposta r on r.id = n1.resposta_id
join exercicio e on e.id = r.exercicio_id
join secao s on s.id = e.secao_id
join aluno a on a.id = r.aluno_id
group by a.nome;

/*Usando IN com sub-query*/
select a.nome, avg(n1.nota) as media, 
avg(n1.nota) - (select avg(n2.nota) from nota n2) as diferenca from 
nota n1 
join resposta r on r.id = n1.resposta_id 
join exercicio e on e.id = r.exercicio_id 
join secao s on s.id = e.secao_id 
join aluno a on a.id = r.aluno_id 
where a.id in 
(select aluno_id from matricula where data > now() - interval 3 month ) group by a.nome;

/*Problema das sub-queries*/
/*
Se a sub-query for mal escrita, ela pode ser executada muitas vezes; 
geralmente uma para cada linha de resposta da "consulta de fora". 
Isso pode fazer com que a consulta leve muito tempo para ser executada, 
podendo causar lentidão do banco de dados e das aplicações que o acessam.
*/

/*Quantidade de matrículas por curso*/
select c.nome, count(m.id), 
count(m.id)/(select count(id) from matricula m)
from curso c join matricula m on m.curso_id = c.id
group by c.nome;
