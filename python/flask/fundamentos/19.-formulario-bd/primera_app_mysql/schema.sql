-- ==========================================================
-- CREACIÓN Y USO DE LA BASE DE DATOS
-- ==========================================================

CREATE DATABASE IF NOT EXISTS primera_flask 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE primera_flask;


-- ==========================================================
-- CREACIÓN DE LA TABLA MASCOTAS
-- ==========================================================

CREATE TABLE IF NOT EXISTS mascotas (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    tipo VARCHAR(255) NOT NULL,
    color VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    updated_at DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- ==========================================================
-- REGISTROS INICIALES DE PRUEBA (OPCIONAL)
-- ==========================================================

INSERT INTO mascotas (nombre, tipo, color, created_at, updated_at) 
VALUES 
    ('Firulais', 'Perro', 'Café', NOW(), NOW()),
    ('Michi', 'Gato', 'Negro', NOW(), NOW());


-- ==========================================================
-- VERIFICACIÓN DE ESTRUCTURA Y DATOS
-- ==========================================================

DESCRIBE mascotas;

SELECT * FROM mascotas;