mysql -uroot -p

/*AULA 1*/
create database controle_compras;
use controle_compras;
/*Criando a tabela*/
create table COMPRAS (id int auto_increment primary key, valor double, data date, 
descricao varchar(255), observacoes varchar(255), recebido boolean);

/*adicionei a tabela dada pelo curso, cap3.sql*/

/*Selecionando apenas alguns atributos*/
SELECT VALOR, OBSERVACOES FROM COMPRAS WHERE DATA >= '2008-12-15';
/*Operador lógico AND com datas*/
SELECT * FROM COMPRAS WHERE DATA >= '2008-12-15' AND DATA < '2010-12-15';
/*Operador lógico AND com data e texto*/
SELECT * FROM COMPRAS WHERE VALOR >= 15.0 AND VALOR <= 35.0 AND OBSERVACOES LIKE 'LANCHONETE%';
/*Filtrando campos booleanos*/
SELECT * FROM COMPRAS WHERE RECEBIDO = 1;
/*Filtrando campos booleanos novamente*/
SELECT * FROM COMPRAS WHERE RECEBIDO = 0;
/*Operador OR*/
SELECT * FROM COMPRAS WHERE RECEBIDO = 1 OR VALOR > 5000.47;
/*Operadores AND e OR juntos*/
SELECT * FROM COMPRAS WHERE (VALOR >= 1000 AND VALOR <= 3000) OR (VALOR > 5000);


/*AULA 2*/

/*UPDATE com WHERE*/
UPDATE COMPRAS SET OBSERVACOES = 'preparando o natal' WHERE DATA = '2010-12-20';
/*Update com cálculo baseado no valor atual de uma coluna*/
update Compras set valor= valor + 10 where data < '2009-06-01';
/*Alteração de várias colunas em um mesmo comando UPDATE*/
UPDATE COMPRAS
      SET OBSERVACOES = 'entregue antes de 2011', RECEBIDO = TRUE
      WHERE DATA BETWEEN '2009-07-01' AND '2010-07-01';
/*DELETE com WHERE*/
DELETE FROM COMPRAS WHERE DATA BETWEEN '2009-03-05' AND '2009-03-20';
/*Operador lógico NOT*/
SELECT * FROM COMPRAS WHERE NOT VALOR = 108;


/*AULA 3*/

/*Colunas do tipo Enum*/
ALTER TABLE COMPRAS ADD COLUMN FORMA_PAGT ENUM('CARTAO', 'BOLETO', 'DINHEIRO');
UPDATE compras SET forma_pagt = 'BOLETO' WHERE forma_pagt IS NULL;
/*Default nas colunas*/
ALTER TABLE COMPRAS MODIFY COLUMN RECEBIDO TINYINT(1) DEFAULT '0';
/*Not Null nas colunas*/
ALTER TABLE COMPRAS MODIFY COLUMN OBSERVACOES TEXT NOT NULL;
/*Reescrevendo o CREATE TABLE*/
CREATE TABLE compras (
          id int NOT NULL AUTO_INCREMENT,
          valor double,
          data datetime,
          observacoes text NOT NULL,
          recebido tinyint(1) DEFAULT 1,
          forma_pagto ENUM('DINHEIRO', 'CARTAO', 'BOLETO'),
          PRIMARY KEY (id)
        );


/*AULA 4*/

/*Calculando a média*/
SELECT AVG(VALOR) FROM COMPRAS WHERE DATA < '2009-05-12';
/*Agrupando por forma de pagamento*/
SELECT FORMA_PAGT, SUM(VALOR) FROM COMPRAS 
        WHERE DATA < '2010-10-10' GROUP BY FORMA_PAGT;
/*Contando número de compras*/
SELECT COUNT(1) FROM COMPRAS WHERE DATA < '2009-05-12' AND RECEBIDO = 1;
/*Agrupando por forma de pagamento*/
SELECT RECEBIDO, FORMA_PAGT, SUM(VALOR) FROM COMPRAS GROUP BY FORMA_PAGT, RECEBIDO;


/*AULA 5*/


/*Criando tabela compradores*/
CREATE TABLE COMPRADORES (ID INT NOT NULL AUTO_INCREMENT, NOME VARCHAR(100) NOT NULL, 
      ENDERECO VARCHAR(100) NOT NULL,
      TELEFONE VARCHAR(20) NOT NULL,
      PRIMARY KEY(ID)
    );
/*Inserindo compradores, e fazendo algumas coisas*/
INSERT INTO COMPRADORES (NOME, ENDERECO, TELEFONE) 
VALUES ('MAURICIO', 'RUA VERGUEIRO, 123', '(11) 1111-1111');
INSERT INTO COMPRADORES (NOME, ENDERECO, TELEFONE) 
VALUES ('ADRIANO', 'AV. PAULISTA, 456', '(11) 2222-2222');
ALTER TABLE COMPRAS ADD COLUMN COMPRADOR_ID INT NOT NULL;
UPDATE COMPRAS SET COMPRADOR_ID = 1 WHERE ID < 8;
UPDATE COMPRAS SET COMPRADOR_ID = 2 WHERE ID >= 8;
/*Nome e valor de todas as compras feitas antes de uma data*/
SELECT NOME, VALOR FROM COMPRAS INNER JOIN COMPRADORES ON COMPRAS.COMPRADOR_ID = COMPRADORES.ID WHERE DATA < '2010-08-09';
/*Compras do comprador com id = 1*/
SELECT * FROM COMPRAS INNER JOIN COMPRADORES ON COMPRAS.COMPRADOR_ID = COMPRADORES.ID WHERE COMPRADOR_ID = 1
/*Exibindo compras dos compradores que se chamam GUILHERME*/
  SELECT COMPRAS.* FROM COMPRAS INNER JOIN COMPRADORES ON COMPRAS.COMPRADOR_ID = COMPRADORES.ID WHERE NOME LIKE 'GUILHERME%';
/*Exibindo compras, agrupando pelo nome do comprador*/
SELECT COMPRADORES.NOME, SUM(VALOR) 
FROM COMPRAS INNER JOIN COMPRADORES ON COMPRAS.COMPRADOR_ID = COMPRADORES.ID GROUP BY COMPRADORES.NOME;
/*FOREIGN KEY*/
ALTER TABLE COMPRAS ADD FOREIGN KEY (COMPRADOR_ID) REFERENCES COMPRADORES(ID);

/*FIM*/

