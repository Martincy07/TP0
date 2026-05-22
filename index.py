def crear_cancha():
    cancha = [["." for columna in range(60)] for fila in range(100)]
    return cancha


def buscar_jugador(jugadores, nombre):
    for jugador in jugadores:
        if jugador["nombre"] == nombre:
            return jugador
    return None


def obtener_poseedor_pelota(jugadores):
    for jugador in jugadores:
        if jugador["tiene_pelota"] == True:
            return jugador
    return None


def agregar_jugador(cancha, jugadores):
    nombre = input("Nombre del jugador: ")

    equipo = input("Equipo (A/B): ")

    while equipo != "A" and equipo != "B":
        print("Error: equipo inválido")
        equipo = input("Equipo (A/B): ")

    fila = int(input("Fila (0-99): "))

    while fila < 0 or fila > 99:
        print("Error: fila inválida")
        fila = int(input("Fila (0-99): "))

    columna = int(input("Columna (0-59): "))

    while columna < 0 or columna > 59:
        print("Error: columna inválida")
        columna = int(input("Columna (0-59): "))

    rol = input("Rol (arquero/defensor/mediocampista/delantero): ")

    while rol not in ["arquero", "defensor", "mediocampista", "delantero"]:
        print("Error: rol inválido")
        rol = input("Rol (arquero/defensor/mediocampista/delantero): ")

    tiene_pelota = input("¿Tiene la pelota? (s/n): ")

    while tiene_pelota != "s" and tiene_pelota != "n":
        print("Error: ingresá s o n")
        tiene_pelota = input("¿Tiene la pelota? (s/n): ")

    tiene_pelota = tiene_pelota == "s"

    if tiene_pelota:
        for jugador in jugadores:
            if jugador["tiene_pelota"] == True:
                print("Error: ya existe un jugador con la pelota")
                return

    if cancha[fila][columna] != ".":
        print("Error: celda ocupada")
        return

    jugador = {
        "nombre": nombre,
        "equipo": equipo,
        "fila": fila,
        "columna": columna,
        "rol": rol,
        "tiene_pelota": tiene_pelota
    }

    jugadores.append(jugador)

    cancha[fila][columna] = equipo

    print("Jugador agregado correctamente")


def mover_jugador(cancha, jugadores):
    nombre = input("Nombre del jugador: ")

    jugador = buscar_jugador(jugadores, nombre)

    if jugador == None:
        print("Jugador no encontrado")
        return False

    direccion = input("Dirección (arriba/abajo/izquierda/derecha): ")

    nueva_fila = jugador["fila"]
    nueva_columna = jugador["columna"]

    if direccion == "arriba":
        nueva_fila -= 1

    elif direccion == "abajo":
        nueva_fila += 1

    elif direccion == "izquierda":
        nueva_columna -= 1

    elif direccion == "derecha":
        nueva_columna += 1

    else:
        print("Dirección inválida")
        return False

    if nueva_fila < 0 or nueva_fila > 99:
        print("Movimiento inválido")
        return False

    if nueva_columna < 0 or nueva_columna > 59:
        print("Movimiento inválido")
        return False

    if cancha[nueva_fila][nueva_columna] != ".":
        print("Celda ocupada")
        return False

    cancha[jugador["fila"]][jugador["columna"]] = "."

    jugador["fila"] = nueva_fila
    jugador["columna"] = nueva_columna

    cancha[nueva_fila][nueva_columna] = jugador["equipo"]

    print("Movimiento realizado correctamente")

    return True


def calcular_distancias(jugadores):
    poseedor = obtener_poseedor_pelota(jugadores)

    if poseedor == None:
        print("No hay ningún jugador con la pelota")
        return

    distancia_minima = None
    jugadores_cercanos = []

    print("\nDistancias a la pelota:")

    for jugador in jugadores:

        distancia = abs(jugador["fila"] - poseedor["fila"]) + abs(jugador["columna"] - poseedor["columna"])

        print(jugador["nombre"], "->", distancia)

        if jugador["nombre"] != poseedor["nombre"]:

            if distancia_minima == None or distancia < distancia_minima:
                distancia_minima = distancia
                jugadores_cercanos = [jugador["nombre"]]

            elif distancia == distancia_minima:
                jugadores_cercanos.append(jugador["nombre"])

    print("\nJugador con la pelota:", poseedor["nombre"])

    if len(jugadores_cercanos) > 0:

        print("Jugador(es) más cercano(s):")

        for nombre in jugadores_cercanos:
            print("-", nombre)

        print("Distancia mínima:", distancia_minima)


def mostrar_cancha(cancha):
    for fila in cancha:
        print(" ".join(fila))


def main():
    cancha = crear_cancha()
    jugadores = []

    opcion = 0

    while opcion != 7:

        print("\n===== MENÚ =====")
        print("1. Agregar jugador")
        print("2. Mover jugador")
        print("3. Calcular distancias")
        print("4. Detectar pases")
        print("5. Camino libre al arco")
        print("6. Ver cancha")
        print("7. Salir")

        opcion = int(input("Elegí una opción: "))

        if opcion == 1:
            agregar_jugador(cancha, jugadores)

        elif opcion == 2:
            mover_jugador(cancha, jugadores)

        elif opcion == 3:
            calcular_distancias(jugadores)

        elif opcion == 6:
            mostrar_cancha(cancha)

        elif opcion == 7:
            print("Programa finalizado")

        else:
            print("Opción inválida")


main()