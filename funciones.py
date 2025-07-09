import datetime

def agregar_nota(usuario, materia, nota, alumnos_db):

    # Validaciones
    if not 1 <= nota <= 10:
        raise ValueError("La nota debe estar entre 1 y 10")
    if usuario not in alumnos_db:
        raise KeyError(f"Usuario {usuario} no registrado")
    if materia not in alumnos_db[usuario]["materias_aprobadas"]:
        return False
    
    # Registro estructurado con fecha
    registro = {
        "materia": materia,
        "nota": nota,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    }
    
    alumnos_db[usuario]["notas"].append(registro)
    return True

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