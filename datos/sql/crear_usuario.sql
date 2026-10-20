CREATE USER IF NOT EXISTS 'usuario_restaurante'@'localhost'
IDENTIFIED BY 'RestauranteLocal2026!';

GRANT SELECT, INSERT, UPDATE, DELETE
ON restaurante.*
TO 'usuario_restaurante'@'localhost';