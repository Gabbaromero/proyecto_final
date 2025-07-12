from database import cargar_alumnos, guardar_alumnos, ALUMNOS
from funciones import agregar_nota, calcular_promedio


def menu_principal():
    print("\nSistema Académico")
    print("1. Agregar nota")
    print("2. Ver promedio")
    print("3. Salir")


def main():
    global ALUMNOS
    ALUMNOS = cargar_alumnos


while True:
    menu_principal()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        usuario = input("Usuario: ")
        materia = input("Materia: ")
        try:
            nota = float(input("Nota (1-10): "))
            if agregar_nota(usuario, materia, nota, ALUMNOS):
                print(" Nota registrada")

            else:
                print("Materia no aprobada")
        except Exception as e:
            print(f" Error: {e}")
    elif opcion == "2":
        usuario = input("Usuario: ")

        try:
            promedio = calcular_promedio(usuario, ALUMNOS)
            print(f" Promedio: {promedio:.2f}")
        except Exception as e:
            print(f" Error: {e}")
    elif opcion == "3":
        print("¡Hasta luego!")
        break

if __name__ == "__main__":
    try:
        main()
    finally:
        guardar_alumnos(ALUMNOS)
