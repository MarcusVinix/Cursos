use sql2

/*Agrupando por aluno por curso*/
select a.nome, c.nome, avg(n.nota) from 
nota n
join resposta r on r.id = n.resposta_id
join exercicio e on e.id = r.exercicio_id
join secao s on s.id = e.secao_id
join curso c on c.id = s.curso_id
join aluno a on a.id = r.aluno_id
group by c.nome, a.nome
having avg(n.nota) < 5;

/*Mais GROUP BY*/
select c.nome, count(m.id) from 
curso c join matricula m on c.id = m.curso_id
group by c.nome
having count(m.id) > 1;

/*Seções por curso*/
select c.nome, count(s.id) from
curso c join secao s on c.id = s.curso_id
group by c.id
having count(s.id) > 3;


