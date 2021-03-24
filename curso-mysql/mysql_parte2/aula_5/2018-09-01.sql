use sql2

/*Usando o DISTINCT*/   
select distinct tipo from matricula;

/*Usando o IN*/
select c.nome, count(m.id) from 
curso c join matricula m on c.id = m.curso_id
where m.tipo in ('PAGA_PF', 'PAGA_PJ')
group by c.nome;

/*Perguntas e respostas com IN*/
select e.pergunta, count(r.id) from
exercicio e join resposta r on e.id = r.exercicio_id
join secao s on s.id = e.secao_id
join curso c on s.curso_id = c.id
where c.id in (1,3)
group by e.pergunta;