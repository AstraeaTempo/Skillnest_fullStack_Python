-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS esquema_usuarios 
DEFAULT CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE esquema_usuarios;

-- Crear la tabla usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insertar datos de prueba opcionales
INSERT INTO usuarios (nombre, apellido, email) VALUES
('Ricky', 'Martin', 'ricky@codingdojo.com'),
('Enrique', 'Iglesias', 'enrique@codingdojo.com'),
('Celia', 'Cruz', 'celia@codingdojo.com'),
('Ricardo', 'Montaner', 'ricardo@codingdojo.com');

-- Verificar la estructura y registros
DESCRIBE usuarios;
SELECT * FROM usuarios;