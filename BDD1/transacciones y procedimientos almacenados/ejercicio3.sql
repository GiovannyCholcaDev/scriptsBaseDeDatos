-- DROP DATABASE IF EXISTS test;
-- CREATE DATABASE test CHARACTER SET utf8mb4;
 -- USE test;

use pumablog

CREATE TABLE cliente (
    id INT UNSIGNED PRIMARY KEY,
    nombre CHAR (20)
);

START TRANSACTION;
INSERT INTO cliente VALUES (2, 'juan');
COMMIT;

-- 1. �Qu� devolver� esta consulta?
SELECT * FROM cliente;

SET AUTOCOMMIT=0;
INSERT INTO cliente VALUES (3, 'Maria');
INSERT INTO cliente VALUES (4, 'Luis');
DELETE FROM cliente WHERE nombre = 'Luis';


-- 2. �Qu� devolver� esta consulta?
SELECT * FROM cliente;


ROLLBACK;

-- 3. �Qu� devolver� esta consulta?
SELECT * FROM cliente;