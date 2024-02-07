CREATE TABLE persona (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    edad INT,
    mail VARCHAR(255)
);


select * from persona p 

INSERT INTO persona (nombre, apellido, edad, mail) VALUES ('Juan', 'Pérez', 30, 'juan@example.com');

INSERT INTO persona (nombre, apellido, edad, mail) VALUES ('María', 'García', 25, 'maria@example.com');

INSERT INTO persona (nombre, apellido, edad, mail) VALUES ('Pedro', 'López', 40, 'pedro@example.com');

INSERT INTO persona (nombre, apellido, edad, mail) VALUES ('Laura', 'Martínez', 35, 'laura@example.com');

INSERT INTO persona (nombre, apellido, edad, mail) VALUES ('Ana', 'Rodríguez', 28, 'ana@example.com');

select * from persona p 