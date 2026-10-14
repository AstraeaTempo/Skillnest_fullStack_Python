# **Cinepedia**

 **Autor:** *Javiera Zapata*  
 **Curso:** *4°C*  
 **Fecha creacion:** *13/10/2026*  

## Tecnologías
- Python/Flask
- MySQL/PyMySql
- HTML
- CSS
- Bootstrap

## Estructura

```text
simulacion1_cinepedia/
│
├── app/
│   ├── config/
│   │   ├── __init__.py
│   │   └── mysqlconnection.py
│   │
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── peliculas_controller.py
│   │   └── usuarios_controller.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── comentario.py
│   │   ├── pelicula.py
│   │   └── usuario.py
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   │
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── editar_pelicula.html
│   │   ├── index.html
│   │   ├── nueva_pelicula.html
│   │   └── pelicula_info.html
│   │
│   └── __init__.py
│
├── resources/
│   └── db/
│       ├── ERD.png
│       └── schema.sql
│
├── .env
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── README.md
└── server.py
```