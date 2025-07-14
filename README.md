# Sistema Académico

Sistema de gestión para instituciones educativas que permite administrar alumnos, materias y calificaciones.

## 🗂️ Estructura del proyecto
proyecto_final/
├── database.py    # Maneja almacenamiento en JSON
├── funciones.py   # Contiene las operaciones académicas
└── main.py        # Punto de entrada del sistema

## 🚀 Funcionalidades principales

- **Alumnos**:
  - Registro con validación de datos
  - Autenticación por usuario/contraseña
  - Consulta de información académica

- **Notas**:
  - Registro de calificaciones (1-10)
  - Cálculo de promedios
  - Historial por materia

- **Datos**:
  - Persistencia en archivo JSON
  - Carga automática al iniciar
  - Copia de seguridad al salir

## 📋 Requisitos

  - Python 3.8 o superior
  - No se requieren librerías externas

## 🛠️ Instalación

1. **Clonar repositorio**:
   ```bash
   git clone https://github.com/Gabbaromero/proyecto_final.git
   cd proyecto_final

   crear y activar el entorno virtual: 
   python -m venv venv
        Windows:
         bash 
venv\Scripts\activate