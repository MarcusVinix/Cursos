use sql2

/*LEFT JOIN*/
select a.nome, r.resposta_dada from 
aluno a left join resposta r on a.id = r.aluno_id;

/*Condição no JOIN*/
select a.nome, r.resposta_dada from 
aluno a left join resposta r on a.id = r.aluno_id
and r.exercicio_id = 1;

/*Diferença entre JOIN e LEFT JOIN*/
O LEFT JOIN favorece a tabela a esquerda da relação. Ou seja, 
mesmo se não existirem elementos na tabela da direita, ele trará a linha.

No JOIN, o elemento deve existir em ambas as tabelas da junção.
