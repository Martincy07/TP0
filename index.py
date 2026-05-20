def crear_cancha():
    # Crea la matriz 100x60 inicializada con "."
    cancha = [["." for columna in range(60)] for fila in range(100)]
    return cancha


def agregar_jugador(cancha, jugadores):
    # Pedir y validar nombre
    nombre = input("Nombre del jugador: ")

    # Pedir y validar equipo
    equipo = input("Equipo (A/B): ")
    while equipo != "A" and equipo != "B":
        print("Error: equipo inválido, debe ser A o B")
        equipo = input("Equipo (A/B): ")

    # Pedir y validar fila
    fila = int(input("Fila (0-99): "))
    while fila < 0 or fila > 99:
        print("Error: la fila debe estar entre 0 y 99")
        fila = int(input("Fila (0-99): "))

    # Pedir y validar columna
    columna = int(input("Columna (0-59): "))
    while columna < 0 or columna > 59:
        print("Error: la columna debe estar entre 0 y 59")
        columna = int(input("Columna (0-59): "))

    # Pedir y validar rol
    roles_validos = ["arquero", "defensor", "mediocampista", "delantero"]
    rol = input("Rol (arquero/defensor/mediocampista/delantero): ")
    while rol not in roles_validos:
        print("Error: rol inválido")
        rol = input("Rol (arquero/defensor/mediocampista/delantero): ")

    # Pedir y validar pelota
    tiene_pelota = input("¿Tiene la pelota? (s/n): ")
    while tiene_pelota != "s" and tiene_pelota != "n":
        print("Error: ingresá s o n")
        tiene_pelota = input("¿Tiene la pelota? (s/n): ")
    tiene_pelota = tiene_pelota == "s"

    # Verificar que no haya otro jugador con la pelota
    if tiene_pelota:
        for jugador in jugadores:
            if jugador["tiene_pelota"] == True:
                print("Error: ya hay un jugador con la pelota")
                return


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
        if cancha[fila][columna] != ".":
            print("Error: la celda está ocupada")
        else:
        # Crear el diccionario del jugador
            jugador = {
                "nombre": nombre,
                "equipo": equipo,
                "fila": fila,
                "columna": columna,
                "rol": rol,
                "tiene_pelota": tiene_pelota
            }
        # Agregar a la lista y actualizar la matriz
        jugadores.append(jugador)
        cancha[fila][columna] = equipo
        print(f"Jugador {nombre} agregado correctamente")    

main()
