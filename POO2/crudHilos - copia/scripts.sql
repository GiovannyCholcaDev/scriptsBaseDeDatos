use pumasblogcuentacuenta;


CREATE TABLE cuentas (
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  numero_cuenta varchar(40) NOT NULL,
  tipo_cuenta varchar(20),
  origen varchar(20),
  fecha DATETIME NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='registra cuentas de los clientes';



INSERT INTO cuentas (numero_cuenta, tipo_cuenta, origen, fecha) VALUES
('1234567890', 'Corriente', 'Nacional', '2023-01-01'),
('9876543210', 'Ahorro', 'Extranjero', '2023-02-15'),
('5678901234', 'Corriente', 'Nacional', '2023-03-20'),
('3456789012', 'Ahorro', 'Nacional', '2023-04-10'),
('9012345678', 'Corriente', 'Extranjero', '2023-05-05');

select * from cuentas;

truncate cuentas;

commit;

select @@autocommit;