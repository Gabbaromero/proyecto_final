from database import cargar_alumnos, guardar_alumnos, ALUMNOS, listar_materias
from funciones import agregar_nota, calcular_promedio, listar_alumnos, verificar_contrasena

def menu_principal():
    """Muestra el menú principal"""
    print("\n=== SISTEMA ACADÉMICO ===")
    print("1. Agregar nota")
    print("2. Ver promedio")
    print("3. Listar materias")
    print("4. Listar alumnos")
    print("5. Salir")

def autenticar_usuario():
    """Maneja el login de usuarios"""
    usuario = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()
    return usuario if verificar_contrasena(usuario, contrasena) else None

def main():
    """Función principal del programa"""
    global ALUMNOS
    ALUMNOS = cargar_alumnos()
    
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":  # Agregar nota
            if (usuario := autenticar_usuario()):
                materia = input("Materia: ").strip()
                try:
                    nota = float(input("Nota (1-10): "))
                    if agregar_nota(usuario, materia, nota, ALUMNOS):
                        print("✓ Nota registrada")
                    else:
                        print("× Materia no aprobada o usuario inválido")
                except ValueError:
                    print("Error: La nota debe ser un número")
            else:
                print("× Credenciales incorrectas")
        
        elif opcion == "2":  # Ver promedio
            if (usuario := autenticar_usuario()):
                try:
                    promedio = calcular_promedio(usuario, ALUMNOS)
                    print(f"★ Promedio: {promedio:.2f}")
                except Exception as e:
                    print(f"Error: {e}")
        
        elif opcion == "3":  # Listar materias
            print(listar_materias())
        
        elif opcion == "4":  # Listar alumnos
            print(listar_alumnos(ALUMNOS))
        
        elif opcion == "5":  # Salir
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    try:
        main()
    finally:
        guardar_alumnos(ALUMNOS)