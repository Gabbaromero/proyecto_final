import datetime
from database import ALUMNOS, validar_alumno


def agregar_nota(usuario, materia, nota, alumnos_db):
    """Validaciones"""
    if not 1 <= nota <= 10:
        raise ValueError("La nota debe estar entre 1 y 10")
    if usuario not in alumnos_db:
        raise KeyError(f"Usuario {usuario} no registrado")
    if materia not in alumnos_db[usuario]["materias_aprobadas"]:
        return False

    """Registro con fecha"""
    registro = {
        "materia": materia,
        "nota": nota,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    alumnos_db[usuario]["notas"].append(registro)
    return True
def listar_alumnos(alumnos_db):
    """
    Lista todos los alumnos registrados en formato legible.

    """
    try:
        if not alumnos_db:
            return "No hay alumnos registrados"
        
        lista = "\nLista de alumnos:\n"
        for usuario, datos in alumnos_db.items():
            lista += f"- {datos['nombre']} {datos['apellido']} (Usuario: {usuario})\n"
        return lista
    
    except Exception as e:
        return f"Error al listar alumnos: {str(e)}"

def obtener_alumno(usuario):
    """Devuelve los datos de un alumno específico"""
    return ALUMNOS.get(usuario)


def verificar_contrasena(usuario, contrasena):
    """Valida las credenciales de acceso"""
    alumno = obtener_alumno(usuario)
    return alumno and alumno["contrasena"] == contrasena


def calcular_promedio(usuario, alumnos_db):
    """Calcula el promedio de un alumno"""
    if usuario not in alumnos_db:
        raise KeyError(f"Usuario {usuario} no existe")
    notas = [registro["nota"] for registro in alumnos_db[usuario]["notas"]]
    return sum(notas) / len(notas) if notas else 0


def registrar_alumno(usuario, nombre, apellido, edad, contrasena):
    try:
        validar_alumno(usuario, nombre, apellido, edad, contrasena)
        ALUMNOS[usuario] = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "contrasena": contrasena,
            "materias_aprobadas": [],
            "notas": []
        }
        return True
    except (TypeError, ValueError) as e:
        print(f"Error al registrar: {e}")
        return False
