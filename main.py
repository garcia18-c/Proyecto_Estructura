from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


def leer_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("  Debe ingresar un número entero.")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("  Este campo no puede quedar vacío.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = leer_texto("  Nombre: ")
    cedula = leer_texto("  Cédula: ")
    edad = leer_entero("  Edad: ")
    while edad < 0:
        print("  La edad no puede ser negativa.")
        edad = leer_entero("  Edad: ")
    fecha = leer_texto("  Fecha de vuelo (AAAA-MM-DD): ")
    destino = leer_texto("  Destino: ")
    asiento = leer_texto("  Asiento: ").upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito", "12A"),
        Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C"),
        Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto", "0934567890", 16, "2026-11-20", "Quito", "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima", "01A")
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


def ejecutar_menu(estructura, titulo, entrar, salir, ver, es_pila):
    while True:
        mostrar_opciones(titulo, entrar, salir, ver)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if estructura.apilar(pasajero) if es_pila else estructura.encolar(pasajero):
                print("  Pasajero agregado correctamente.")
        elif op == "2":
            estructura.listar()
        elif op == "3":
            pasajero = estructura.desapilar() if es_pila else estructura.desencolar()
            if pasajero is None:
                print("  La estructura está vacía.")
            else:
                print("  Salió:", pasajero)
        elif op == "4":
            pasajero = estructura.ver_tope() if es_pila else estructura.ver_frente()
            if pasajero is None:
                print("  La estructura está vacía.")
            else:
                print("  Tope:" if es_pila else "  Frente:", pasajero)
        elif op == "5":
            numero = leer_entero("  Número de pasajero que desea buscar: ")
            posicion = estructura.buscar(numero)
            if posicion == -1:
                print("  El pasajero no existe.")
            else:
                print(f"  Encontrado en [{posicion}]: {estructura.datos[posicion]}")
        elif op == "6":
            numero = leer_entero("  Número de pasajero que desea modificar: ")
            destino = leer_texto("  Nuevo destino: ")
            asiento = leer_texto("  Nuevo asiento: ").upper()
            if estructura.modificar(numero, destino, asiento):
                print("  Pasajero modificado correctamente.")
            else:
                print("  El pasajero no existe.")
        elif op == "7":
            numero = leer_entero("  Número de pasajero que desea eliminar: ")
            pasajero = estructura.eliminar_por_numero(numero)
            if pasajero is None:
                print("  El pasajero no existe o la estructura está vacía.")
            else:
                print("  Pasajero eliminado:", pasajero)
        elif op == "8":
            copia = estructura.copiar()
            print("  Copia creada. Contenido:")
            copia.listar()
        elif op == "9":
            print("  Longitud:", estructura.longitud())
            if estructura.esta_vacia():
                print("  La estructura está vacía.")
            else:
                print("  La estructura no está vacía.")
        elif op == "C":
            for pasajero in datos_prueba():
                if es_pila:
                    estructura.apilar(pasajero)
                else:
                    estructura.encolar(pasajero)
            print("  Datos de prueba cargados. Los números repetidos no se agregan.")
        elif op == "0":
            break
        else:
            print("  Opción no válida.")


def menu_pila():
    ejecutar_menu(pila, "MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar",
                  "Ver tope", True)


def menu_cola():
    ejecutar_menu(cola, "MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar",
                  "Ver frente", False)


def main():
    while True:
        print("\\n===== TAREA PILAS Y COLAS · PASAJEROS =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
