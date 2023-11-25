from crud_archivo import eliminar_partida, agregar_partida, listar_partidas

tablero = [[0] * 3 for i in range(3)]

def mostrar_tablero() :
  for i in range(3) :
    for j in range(3) :
      print(end= f"{tablero[i][j]}  ")
    print("")


def agregar_pieza(jugador) :
  print("")
  print(f"Turno del jugador {jugador['nombre']}")
  print("➡️ Ingrese el numero de fila y numero de columna donde quiere poner su ficha")
  while ValueError :
    try :
      f = int(input("fila: ")) - 1
      c = int(input("columna: ")) - 1
      while not f in [0, 1, 2] or not c in [0, 1, 2] :
        print("❌ El numero no puede ser mayor a 3 ni menor que 1")
        f = int(input("fila: ")) - 1
        c = int(input("columna: ")) - 1
    except ValueError :
      print("❌ Solo puedes ingresar numeros")
    else : 
      if not tablero[f][c] :
        tablero[f][c] = jugador["ficha"]
        break
      else :
        print("❌ Esta casilla ya esta ocupada, Ingrese otra posición")

def tablero_texto(tablero: list) :
  tab = ""
  for i in range(3):
    for j in range(3):
      tab += f"{(tablero[i][j])}"
  return tab

def calcular_ganador(tablero: list, jugador1: dict, jugador2: dict):
  tab = []
  for i in range(3):
    for j in range(3):
      tab.append(tablero[i][j])
  tab
  posicionesGanadoras = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ] 
  for posiciones in posicionesGanadoras:
    pos1, pos2 , pos3 = posiciones
    if tab[pos1] and tab[pos1] == tab[pos2] == tab[pos3]:
      return jugador1["nombre"] if tab[pos1] == "X" else jugador2["nombre"]
  
  return False



def jugar_tateti() :
  print("🔠 Ingrese los nombres de los jugadores.")
  jugador1 = {"nombre": input("Jugador 1️⃣: "), "ficha": "X"}
  jugador2 = {"nombre": input("Jugador 2️⃣: "), "ficha": "O"}

  while not calcular_ganador(tablero=tablero, jugador1=jugador1, jugador2=jugador2) :

    agregar_pieza(jugador1)
    mostrar_tablero()
    if not calcular_ganador(tablero=tablero, jugador1=jugador1, jugador2=jugador2) :
      agregar_pieza(jugador2)
      mostrar_tablero()

  ganador = calcular_ganador(tablero=tablero, jugador1=jugador1, jugador2=jugador2)
  print('El ganador es', ganador)

  agregar_partida({"JUGADOR1": jugador1["nombre"],"JUGADOR2": jugador2["nombre"], "GANADOR":ganador, "RESULTADO": tablero_texto(tablero)})

def mostrar_partidas() :
  partidas = listar_partidas()
  for partida in partidas :
    print("")
    print(f"Partida N° {partida['ID']}")
    print(f"Jugador 1️⃣: {partida['JUGADOR1']} (X) | Jugador 2️⃣: {partida['JUGADOR2']} (O)") 
    print("")
    resultado = list(partida["RESULTADO"])
    for i in range(9) :
      print(end=f"{resultado[i]}  ")
      if (i + 1) % 3 == 0:
        print("")
    
    print(f"🏆 Ganador: {partida['GANADOR']}")

print("Bienvenido al ta-te-ti")

while ValueError :
  print("\n📖 Si quiere ver las partidas anteriores ingrese '1' por consola")
  print("🕹️ Si quiere jugar al juego ingrese '2' por consola")
  print("🔴 Para salir del programa ingrese '0' por consola")
  try :
    pregunta = int(input("Ingrese un numero: "))
    while pregunta > 2 or pregunta < 0:
      print("ERROR: Solo puedes ingresar 0, 1 o 2")
      pregunta = int(input("Ingrese un numero: "))
  except ValueError :
    print("ERROR: Solo puedes ingresar numeros")
  else :
    if pregunta == 1 :
      mostrar_partidas()
    elif pregunta == 2 :
      jugar_tateti()
    else : 
      break

    
