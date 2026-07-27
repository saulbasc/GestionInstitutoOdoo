# Gestión Instituto - Odoo 16

Módulo desarrollado para Odoo 16 que permite gestionar la información básica de un instituto.

<img width="633" height="336" alt="Menú principal" src="https://github.com/user-attachments/assets/eca9c241-36da-4168-a663-cd0049299b9d" />

## Funcionalidades

- Gestión de estudiantes.
- Gestión de profesores.
- Gestión de cursos.
- Gestión de grupos.
- Gestión de asignaturas.
- Gestión de horarios.
- Gestión de calificaciones.
  
## Validaciones

- Validación del DNI para comprobar que es correcto.
- Validación de la nota para que se encuentre dentro del rango permitido.
- Validación de fechas para garantizar que se encuentran dentro del rango correspondiente.
- Validación de relaciones entre entidades para asegurar la consistencia de los datos.
- Validaciones adicionales en campos de selección y listas desplegables para garantizar la coherencia de los datos.

## Tecnologías

- Odoo 16
- Python
- XML
- PostgreSQL
- Docker

## Instalación

1. Clonar el repositorio en la carpeta de addons de Odoo.
2. Reiniciar el servidor de Odoo.
3. Actualizar la lista de aplicaciones.
4. Instalar el módulo **Instituto** desde el menú **Aplicaciones**.
