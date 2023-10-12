#create database banco_financeiro;
USE banco_financeiro;


CREATE TABLE tbl_app(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
cnpj_app CHAR(14) NOT NULL,
endereco_app VARCHAR(50) NOT NULL,
telefone_app CHAR(8),

fk_id_plano INT NOT NULL,
fk_id_contador INT NOT NULL,
fk_id_usuario INT NOT NULL
);

#alter table tbl_app add constraint fk_id_usuarioApp foreign key (fk_id_usuario) references tbl_usuario (id_usuario);

CREATE TABLE tbl_plano_plus(
id_plano INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nome_plano VARCHAR(50) NOT NULL,
valor_plano DECIMAL NOT NULL,

fk_id_contador INT NOT NULL,
fk_id_usuario INT NOT NULL
);

#alter table tbl_plano_plus add constraint fk_id_usuarioPlus foreign key (fk_id_usuario) references tbl_usuario (id_usuario);

CREATE TABLE tbl_contador(
id_contador INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nome_contador VARCHAR(100) NOT NULL,
data_nasc_contador DATE NOT NULL,
cpf_contador CHAR(11) NOT NULL,
telefone_contador VARCHAR(10) NOT NULL,
email_contador VARCHAR(100) NOT NULL,
senha_contador VARCHAR(50) NOT NULL,
contribuicao_contador DECIMAL NOT NULL,
valor_aulas_contador DECIMAL NOT NULL,
status_contador BOOLEAN NOT NULL
);

CREATE TABLE tbl_usuario(
id_usuario INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nome_usuario VARCHAR(100) NOT NULL,
data_nasc_usuario DATE NOT NULL,
cpf_usuario CHAR(11) NOT NULL,
telefone_usuario VARCHAR(11) NOT NULL,
email_usuario VARCHAR(100) NOT NULL,
senha_usuario VARCHAR(1000) NOT NULL,
saldo_atual_usuario DECIMAL,
status_usuario BOOLEAN
);
SELECT * FROM tbl_usuario;

CREATE TABLE tbl_despesa_mensal(
id_despesa_mensal INT PRIMARY KEY AUTO_INCREMENT,
nome_despesa_mensal VARCHAR(40) NOT NULL,
desc_despesa_mensal VARCHAR(150),
valor_despesa_mensal DECIMAL NOT NULL,

fk_id_usuario INT NOT NULL
);

#alter table tbl_despesa_mensal add constraint fk_id_usuarioD foreign key (fk_id_usuario) references tbl_usuario (id_usuario);

CREATE TABLE tbl_renda_mensal(
id_renda_mensal INT PRIMARY KEY AUTO_INCREMENT,
nome_renda_mensal VARCHAR(40) NOT NULL,
desc_renda_mensal VARCHAR(150),
valor_renda_mensal DECIMAL NOT NULL,

fk_id_usuario INT NOT NULL
);

#alter table tbl_renda_mensal add constraint fk_id_usuarioR foreign key (fk_id_usuario) references tbl_usuario (id_usuario);

CREATE TABLE tbl_pagamentos(
id_pagamento INT PRIMARY KEY AUTO_INCREMENT,
desc_pagamento VARCHAR(300) NOT NULL,
valor_pagamento DECIMAL NOT NULL,
data_vencimento_pagamento DATE,

fk_id_usuario INT NOT NULL,
FOREIGN KEY(fk_id_usuario) REFERENCES tbl_usuario(id_usuario)
);
SELECT * FROM tbl_pagamentos;


#alter table tbl_calendario add constraint fk_id_usuarioC foreign key (fk_id_usuario) references tbl_usuario (id_usuario);

CREATE TABLE tbl_cartao_de_credito(
limite DECIMAL, 
renovacao DATE, 
parcelas INT,
preco DECIMAL,

fk_id_usuario INT NOT NULL
);

#alter table tbl_cartao_de_credito add constraint fk_id_usuarioCdC foreign key (fk_id_usuario) references tbl_usuario (id_usuario);


SELECT * FROM tbl_usuario;
SELECT * FROM tbl_renda_mensal;
SELECT * FROM tbl_despesa_mensal;

SELECT nome_renda_mensal, valor_renda_mensal FROM tbl_renda_mensal WHERE fk_id_usuario = 1;

UPDATE tbl_renda_mensal SET valor_renda_mensal = "2000" WHERE nome_renda_mensal = "Salario" AND fk_id_usuario = 1;