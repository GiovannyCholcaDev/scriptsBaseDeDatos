CREATE TABLE cuentas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo CHAR (20),
    sumavalor decimal (5,2)
);

select * from cuentas;
select * from roles;

insert into cuentas (tipo, sumavalor) values ('rol',10.1);

start transaction;
	select @total:=sum(salario) from roles;
    -- modificar valor
	set @total:= @total + 10;

	update cuentas set sumavalor = @total where id = 1;
commit;
	


