import json


ALUMNOS = {
    "caroliv": {
        "nombre": "Carlos",
        "apellido": "Olivera",
        "edad": 25,
        "contrasena": "ca1234",
        "materias_aprobadas": [
            "Matemática", "Contabilidad", "Estadística I"
        ],
        "notas": [
            {"materia": "Matemática", "nota": 8, "fecha": "2025-03-15"},
            {"materia": "Contabilidad", "nota": 9, "fecha": "2025-04-20"},
            {"materia": "Estadística I", "nota": 7, "fecha": "2025-05-10"}
        ]
    },
    "silvi56": {
        "nombre": "Silvina",
        "apellido": "Perez",
        "edad": 28,
        "contrasena": "silper",
        "materias_aprobadas": [
            "Matemática", "Álgebra I", "Filosofía"
        ],
        "notas": [
            {"materia": "Matemática", "nota": 7, "fecha": "2025-03-18"},
            {"materia": "Álgebra I", "nota": 8, "fecha": "2025-04-22"}
        ]
    },
    "brumar": {
        "nombre": "Bruno",
        "apellido": "Martinez",
        "edad": 23,
        "contrasena": "bm8754",
        "materias_aprobadas": [
            "Matemática", "Estadística I", "Estadística II",
            "Introducción a la Economía", "Microeconomía"
        ],
        "notas": [
            {"materia": "Matemática", "nota": 8, "fecha": "2025-03-10"},
            {"materia": "Estadística I", "nota": 9, "fecha": "2025-04-05"},
            {"materia": "Estadística II", "nota": 6, "fecha": "2025-05-12"},
            {"materia": "Introducción a la Economía", "nota": 10,
             "fecha": "2025-06-08"},
            {"materia": "Microeconomía", "nota": 7, "fecha": "2025-07-15"}
        ]
    },
    "san79": {
        "nombre": "Santiago",
        "apellido": "Saldivar",
        "edad": 42,
        "contrasena": "sasa34",
        "materias_aprobadas": [
            "Matemática", "Contabilidad", "Estadística I", "Filosofía",
            "Estadística II", "Álgebra I", "Microeconomía", "Macroeconomía"
        ],
        "notas": [
            {"materia": "Matemática", "nota": 10, "fecha": "2025-02-20"},
            {"materia": "Contabilidad", "nota": 9, "fecha": "2025-03-15"},
            {"materia": "Estadística I", "nota": 9, "fecha": "2025-04-10"},
            {"materia": "Filosofía", "nota": 10, "fecha": "2025-05-05"},
            {"materia": "Estadística II", "nota": 8, "fecha": "2025-06-12"},
            {"materia": "Álgebra I", "nota": 9, "fecha": "2025-07-18"},
            {"materia": "Microeconomía", "nota": 8, "fecha": "2025-08-22"},
            {"materia": "Macroeconomía", "nota": 10, "fecha": "2025-09-30"}
        ]
    }
}


MATERIAS_DISPONIBLES = {
    "MAT": "Matemática",
    "ALI": "Álgebra I",
    "ESTI": "Estadística I",
    "ESTII": "Estadística II",
    "MIE": "Microeconomía",
    "MAE": "Macroeconomía"
}


TURNOS = {
    "manana": "08:00 a 12:00",
    "tarde": "13:00 a 17:00",
    "noche": "18:00 a 22:00"
}


ARCHIVO_ALUMNOS = "alumnos.json"


def validar_alumno(usuario, nombre, apellido, edad, contrasena):
    """Valida los datos de un alumno antes de registrarlo"""
    if not isinstance(edad, int):
        raise TypeError(f"La edad debe ser un número entero (se recibió "
                      f"{type(edad)})")
    if edad < 0:
            raise ValueError("La edad no puede ser negativa")
    if edad > 100:
        raise ValueError("Edad inválida: demasiado alta")


def guardar_alumnos():
    """Guarda los datos de los alumnos en un archivo JSON"""
    with open(ARCHIVO_ALUMNOS, 'w') as archivo:
        json.dump(ALUMNOS, archivo, indent=4)
    print("Datos guardados correctamente")


def cargar_alumnos():
    """Carga los datos de alumnos desde el archivo JSON"""
    global ALUMNOS
    try:
        with open(ARCHIVO_ALUMNOS, 'r') as archivo:
            ALUMNOS = json.load(archivo)
        print("Datos cargados correctamente")
    except FileNotFoundError:
        print("No existe el archivo, empezando con datos vacíos")
        ALUMNOS = {}
    except json.JSONDecodeError:
        print("Error leyendo el archivo, empezando con datos vacíos")
        ALUMNOS = {}
