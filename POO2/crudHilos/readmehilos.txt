
select @@autocommit;

SHOW VARIABLES LIKE 'max_connections';

SHOW STATUS LIKE 'Threads_connected';

SELECT CONCAT('KILL ', id, ';') AS query
FROM information_schema.processlist
WHERE user = 'nombre_usuario' AND db = 'nombre_basedatos';
