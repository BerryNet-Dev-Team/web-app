-- init.sql
CREATE DATABASE IF NOT EXISTS mi_base_de_datos;

CREATE USER 'user1'@'192.168.1.252' IDENTIFIED BY 'password1';
GRANT ALL PRIVILEGES ON mi_base_de_datos.* TO 'user1'@'%';

CREATE USER 'user2'@'%' IDENTIFIED BY 'password2';
GRANT ALL PRIVILEGES ON mi_base_de_datos.* TO 'user2'@'%';

FLUSH PRIVILEGES;