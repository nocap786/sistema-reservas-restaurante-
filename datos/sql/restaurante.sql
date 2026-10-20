CREATE DATABASE IF NOT EXISTS restaurante;
USE restaurante;

CREATE TABLE IF NOT EXISTS restaurantes (
    id_restaurante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(150) NOT NULL,
    horario_apertura TIME NOT NULL,
    horario_cierre TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS mesas (
    id_mesa INT AUTO_INCREMENT PRIMARY KEY,
    numero INT NOT NULL,
    capacidad INT NOT NULL,
    caracteristicas VARCHAR(150),
    id_restaurante INT NOT NULL,
    FOREIGN KEY (id_restaurante)
        REFERENCES restaurantes(id_restaurante)
);

CREATE TABLE IF NOT EXISTS reservas (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_mesa INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    cantidad_personas INT NOT NULL,
    estado VARCHAR(20) DEFAULT 'Pendiente',
    FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_mesa)
        REFERENCES mesas(id_mesa)
);