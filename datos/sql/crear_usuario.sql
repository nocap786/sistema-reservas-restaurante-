-- Cambie 'tu_contraseña' por la contraseña que dejara en su archivo .env
CREATE USER IF NOT EXISTS 'usuario_restaurante'@'localhost'
IDENTIFIED BY 'tu_contraseña';

GRANT SELECT, INSERT, UPDATE, DELETE
ON restaurante.*
TO 'usuario_restaurante'@'localhost';
