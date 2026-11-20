"""
Trabajo Práctico Integrador - Gestión de Países
Materia: Programación 1
"""

import csv

NOMBRE_ARCHIVO = "paises.csv"
CAMPOS_CSV = ["nombre", "poblacion", "superficie", "continente"]


# ---------------------------------------------------------
# PERSISTENCIA (CARGA Y GUARDADO DE CSV)
# ---------------------------------------------------------

def cargar_paises():
    """Carga los países desde el archivo CSV. Maneja FileNotFoundError sin 'os'."""
    paises = []
    try:
        with open(NOMBRE_ARCHIVO, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                paises.append({
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                })
        print(f"Se cargaron {len(paises)} países correctamente.")
    except FileNotFoundError:
        print(f"Archivo '{NOMBRE_ARCHIVO}' no encontrado. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    return paises


def guardar_paises(paises):
    """Escribe la lista de países en el archivo CSV."""
    try:
        with open(NOMBRE_ARCHIVO, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_CSV)
            escritor.writeheader()
            escritor.writerows(paises)
        print("Cambios guardados en el archivo CSV.")
    except Exception as e:
        print(f"Error al guardar en el CSV: {e}")


# ---------------------------------------------------------
# VALIDACIONES DE ENTRADA
# ---------------------------------------------------------

def pedir_entero_positivo(mensaje):
    """Solicita un número entero mayor o igual a cero (Ej: 45000000)."""
    while True:
        try:
            val = int(input(mensaje).strip())
            if val >= 0:
                return val
            print("Error: Debe ingresar un número mayor o igual a cero.")
        except ValueError:
            print("Error: Entrada inválida. Ingrese un número entero.")


def pedir_texto_no_vacio(mensaje):
    """Solicita un texto y valida que no esté vacío (Ej: 'Argentina')."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: Este campo no puede estar vacío.")


# ---------------------------------------------------------
# FUNCIONALIDADES DEL MENÚ
# ---------------------------------------------------------

def agregar_pais(paises):
    """1. Agrega un nuevo país al sistema."""
    print("\n--- Agregar País ---")
    nombre = pedir_texto_no_vacio("Nombre: ")
    poblacion = pedir_entero_positivo("Población: ")
    superficie = pedir_entero_positivo("Superficie (km²): ")
    continente = pedir_texto_no_vacio("Continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    guardar_paises(paises)
    print(f"País '{nombre}' agregado exitosamente.")


def actualizar_pais(paises):
    """2. Modifica la población y superficie de un país existente."""
    print("\n--- Actualizar País ---")
    busqueda = input("Nombre del país a modificar: ").strip().lower()

    coincidencias = [p for p in paises if busqueda in p["nombre"].lower()]
    if not coincidencias:
        print("No se encontró ningún país con ese nombre.")
        return

    pais = coincidencias[0]
    print(f"Modificando '{pais['nombre']}' (Población actual: {pais['poblacion']}, Superficie actual: {pais['superficie']} km²)")

    pob_input = input("Nueva población (presione Enter para mantener actual): ").strip()
    sup_input = input("Nueva superficie (presione Enter para mantener actual): ").strip()

    if pob_input:
        try:
            val = int(pob_input)
            if val >= 0:
                pais["poblacion"] = val
            else:
                print("Valor negativo ignorado.")
        except ValueError:
            print("Valor numérico inválido ignorado.")

    if sup_input:
        try:
            val = int(sup_input)
            if val >= 0:
                pais["superficie"] = val
            else:
                print("Valor negativo ignorado.")
        except ValueError:
            print("Valor numérico inválido ignorado.")

    guardar_paises(paises)
    print(f"Datos de '{pais['nombre']}' actualizados correctamente.")


def buscar_pais(paises):
    """3. Búsqueda por coincidencia parcial de nombre."""
    print("\n--- Buscar País ---")
    busqueda = input("Ingrese nombre o parte del nombre: ").strip().lower()
    resultados = [p for p in paises if busqueda in p["nombre"].lower()]

    if resultados:
        print(f"\nResultados encontrados ({len(resultados)}):")
        for p in resultados:
            print(f"- {p['nombre']} | Población: {p['poblacion']:,} | Superficie: {p['superficie']:,} km² | Continente: {p['continente']}")
    else:
        print("No se encontraron coincidencias.")


def filtrar_paises(paises):
    """4. Filtra países por continente, población o superficie."""
    print("\n--- Filtrar Países ---")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    opcion = input("Elija una opción (1-3): ").strip()

    if opcion == "1":
        continente = input("Continente a buscar: ").strip().lower()
        filtrados = [p for p in paises if p["continente"].lower() == continente]
    elif opcion == "2":
        min_pob = pedir_entero_positivo("Población mínima: ")
        max_pob = pedir_entero_positivo("Población máxima: ")
        filtrados = [p for p in paises if min_pob <= p["poblacion"] <= max_pob]
    elif opcion == "3":
        min_sup = pedir_entero_positivo("Superficie mínima: ")
        max_sup = pedir_entero_positivo("Superficie máxima: ")
        filtrados = [p for p in paises if min_sup <= p["superficie"] <= max_sup]
    else:
        print("Opción inválida.")
        return

    if filtrados:
        print(f"\nResultados del filtro ({len(filtrados)} países):")
        for p in filtrados:
            print(f"- {p['nombre']} ({p['continente']}): {p['poblacion']:,} hab / {p['superficie']:,} km²")
    else:
        print("No hay países que cumplan con el criterio ingresado.")


def ordenar_paises(paises):
    """5. Ordena la lista según el criterio y sentido seleccionado."""
    print("\n--- Ordenar Países ---")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    criterio = input("Elija criterio (1-3): ").strip()

    if criterio == "1":
        key_func = lambda x: x["nombre"].lower()
    elif criterio == "2":
        key_func = lambda x: x["poblacion"]
    elif criterio == "3":
        key_func = lambda x: x["superficie"]
    else:
        print("Criterio inválido.")
        return

    sentido = input("¿Orden ascendente? (s/n): ").strip().lower()
    reverse = sentido not in ("s", "si", "sí")

    ordenados = sorted(paises, key=key_func, reverse=reverse)

    print("\nPaíses ordenados:")
    for p in ordenados:
        print(f"- {p['nombre']}: {p['poblacion']:,} hab | {p['superficie']:,} km² | {p['continente']}")


def mostrar_estadisticas(paises):
    """6. Calcula y muestra estadísticas generales."""
    print("\n--- Estadísticas ---")
    if not paises:
        print("No hay datos cargados para calcular estadísticas.")
        return

    mayor_pob = max(paises, key=lambda x: x["poblacion"])
    menor_pob = min(paises, key=lambda x: x["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    conteo_cont = {}
    for p in paises:
        cont = p["continente"]
        conteo_cont[cont] = conteo_cont.get(cont, 0) + 1

    print(f"Mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,} hab)")
    print(f"Menor población: {menor_pob['nombre']} ({menor_pob['poblacion']:,} hab)")
    print(f"Promedio de población: {prom_pob:,.0f} hab")
    print(f"Promedio de superficie: {prom_sup:,.0f} km²")
    print("Países por continente:")
    for cont, cant in conteo_cont.items():
        print(f"  - {cont}: {cant}")


# ---------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------

def main():
    """Bucle principal de la consola."""
    paises = cargar_paises()

    while True:
        print("\n" + "=" * 35)
        print("   MENÚ PRINCIPAL - GESTIÓN PAÍSES")
        print("=" * 35)
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            print("\n¡Programa finalizado!")
            break
        else:
            print("Opción inválida. Intente con un número del 1 al 7.")


if __name__ == "__main__":
    main()
