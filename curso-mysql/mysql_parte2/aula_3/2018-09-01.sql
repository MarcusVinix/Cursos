use sql2

/*GROUP BY*/
select c.nome, avg(n.nota) from 
nota n
join resposta r on r.id = n.resposta_id
join exercicio e on e.id = r.exercicio_id
join secao s on s.id = e.secao_id
join curso c on c.id = s.curso_id
group by c.nome;


/*COUNT de matrículas*/
select c.nome, count(m.id) from 
curso c join matricula m on c.id = m.curso_id
group by c.nome;

/*GROUP BY com WHERE*/
select c.nome, avg(n.nota) from 
nota n
join resposta r on r.id = n.resposta_id
join exercicio e on e.id = r.exercicio_id
join secao s on s.id = e.secao_id
join curso c on c.id = s.curso_id
join aluno a on a.id = r.aluno_id
where a.nome like '%Santos%' or a.nome like '%Silva%'
group by c.nome;

/*mais GROUP BY*/
select e.pergunta, count(r.id) from
exercicio e join resposta r on e.id = r.exercicio_id
group by e.id

/*Ordenando pelo COUNT*/
select e.pergunta, count(r.id) from
exercicio e join resposta r on e.id = r.exercicio_id
group by e.id
order by count(r.id) desc;

/*Agrupando por 2 campos*/
select a.nome, c.nome, avg(n.nota) from 
nota n
join resposta r on r.id = n.resposta_id
join exercicio e on e.id = r.exercicio_id
join secao s on s.id = e.secao_id
join curso c on c.id = s.curso_id
join aluno a on a.id = r.aluno_id
group by c.nome, a.nome;