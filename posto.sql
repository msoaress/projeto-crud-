CREATE database ERP_POSTO;
use ERP_POSTO;

-- CRIAÇÃO DOS BANCOS --
CREATE TABLE LOGIN 
( 

 CNPJ INT,  
 SENHA_APP INT,  
 ID INT PRIMARY KEY
); 

CREATE TABLE ESTOQUE_SAÍDA 
( 
 ID INT  PRIMARY KEY,  
 CÓD_BOMBA int ,  
 DIESEL INT
); 

CREATE TABLE VENDAS 
( 
 ID INT PRIMARY KEY,  
 BOMBAS_POSTO INT,  
 DATA_HORAS INT,  
 CÓD_BOMBA INT ,  
 DIESEL INT,  
 ÁLCOOL INT,  
 GASOLINA INT,
 GNV INT
); 

CREATE TABLE CUSTOS 
( 
 ID INT PRIMARY KEY,  
 FUNCIONÁRIOS INT,  
 PRODUTOS INT,  
 CÓD_BOMBA INT ,  
 ALCOOL INT
); 

CREATE TABLE LUCRO_MENSAL 
( ID int PRIMARY KEY,
 DATA_MÊS INT,  
 LUCRO_REAL INT,  
 CUSTOS INT,  
 CÓD_BOMBA INT  
);

-- INSERINDO DADOS NA TABELA --
------ login ------
INSERT INTO login
VALUES
('456786', '552', '1');
SELECT * FROM login;

INSERT INTO login
VALUES
('234567', '662', '2');
SELECT * FROM login;

------- estoque saída -------
INSERT INTO ESTOQUE_SAÍDA 
VALUES
('1', '890', '011234');
SELECT * FROM ESTOQUE_SAÍDA;

INSERT INTO ESTOQUE_SAÍDA 
VALUES
('2', '888', '456784');
SELECT * FROM ESTOQUE_SAÍDA;

-------  vendas  -------
INSERT INTO VENDAS
VALUES
('1', '890', '24052422','890', '011234', '098908', '890789', '567456');
SELECT * FROM VENDAS;

INSERT INTO VENDAS
VALUES
('2', '888', '25052419','888', '456784', '098909', '890790', '567457');
SELECT * FROM VENDAS;

------ custos -----
INSERT INTO CUSTOS
VALUES
('1', '7089', '1500', '011234', '098908');
SELECT * FROM CUSTOS;  

INSERT INTO CUSTOS
VALUES
('2', '8909', '5000', '456784', '098909');
SELECT * FROM CUSTOS;

------- lucro mensal ------
INSERT INTO LUCRO_MENSAL
VALUES
('1,''240524', '50000', '20000', '890');
SELECT * FROM LUCRO_MENSAL;

INSERT INTO LUCRO_MENSAL
VALUES
('2','250624', '800000', '100000', '888');
SELECT * FROM LUCRO_MENSAL;
