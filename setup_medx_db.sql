-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS medx_db;
CREATE USER IF NOT EXISTS 'medx_dev'@'localhost' IDENTIFIED BY 'betty';
GRANT ALL PRIVILEGES ON `medx_db`.* TO 'medx_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'medx_dev'@'localhost';
FLUSH PRIVILEGES;