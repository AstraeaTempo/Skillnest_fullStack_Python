-- ==========================================================
-- CREAR BASE DE DATOS Y USARLA
-- ==========================================================

CREATE DATABASE IF NOT EXISTS esquema_tacos;

USE esquema_tacos;


-- ==========================================================
-- TABLA RESTAURANTES
-- ==========================================================

CREATE TABLE IF NOT EXISTS restaurantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);


-- ==========================================================
-- TABLA TACOS
-- ==========================================================

CREATE TABLE IF NOT EXISTS tacos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tortilla VARCHAR(45) NOT NULL,
    guiso VARCHAR(45) NOT NULL,
    salsa VARCHAR(45) NOT NULL,
    restaurante_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_tacos_restaurantes
        FOREIGN KEY (restaurante_id)
        REFERENCES restaurantes(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


-- ==========================================================
-- DATOS DE PRUEBA: RESTAURANTES
-- ==========================================================

INSERT INTO restaurantes (id, nombre) VALUES
(1, 'Tacos El Sol'),
(2, 'Tacos Central'),
(3, 'Tacos Don Pepe');


-- ==========================================================
-- DATOS DE PRUEBA: TACOS
-- ==========================================================

INSERT INTO tacos (tortilla, guiso, salsa, restaurante_id) VALUES
('Maíz', 'Carne', 'Verde', 1),
('Harina', 'Pollo', 'Roja', 1),
('Maíz', 'Carnitas', 'Verde', 2),
('Maíz', 'Pastor', 'Picante', 2),
('Harina', 'Barbacoa', 'Roja', 3);