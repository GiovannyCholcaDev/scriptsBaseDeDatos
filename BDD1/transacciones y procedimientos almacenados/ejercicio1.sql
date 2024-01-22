create database pumablog

use pumablog

DROP  table roles

CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre CHAR (20),
    salario decimal (5,2)
);


select * from roles;

insert into roles (nombre, salario) values ('valor1',10.1);

SELECT @@AUTOCOMMIT;

-- guarda automaticamente
SET AUTOCOMMIT = 1;

SET AUTOCOMMIT = 0;


insert into roles (nombre, salario) values ('valor3',3), ('valor4',4);


select * from roles;

 ROLLBACK;

select * from roles;


insert into roles (nombre, salario) values ('valor5',5), ('valor6',6);

commit;

select * from roles;



start transaction;
	update roles set salario = 12 where id = 1;
COMMIT;



