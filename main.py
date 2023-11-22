tablero = [[0] * 3 for i in range(3)]

def mostrar_tablero() :
  for i in range(3) :
    for j in range(3) :
      print(end= f"{tablero[i][j]}")
    print("")

print("Ingrese los nombres de los jugadores.")
jugador1 = {"nombre": input("Jugador 1: "), "ficha": "X"}
jugador2 = {"nombre": input("Jugador 2: "), "ficha": "O"}

def agregar_pieza(jugador) :
  print("")
  print(f"Turno del jugador {jugador['nombre']}")
  print("Ingrese el numero de fila y numero de columna donde quiere poner su ficha")
  while ValueError :
    try :
      f = int(input("fila: ")) - 1
      c = int(input("columna: ")) - 1
      while not f in [0, 1, 2] or not c in [0, 1, 2] :
        print("El numero no puede ser mayor a 3 ni menor que 1")
        f = int(input("fila: ")) - 1
        c = int(input("columna: ")) - 1
    except ValueError :
      print("Solo puedes ingresar numeros")
    else : 
      if not tablero[f][c] :
        tablero[f][c] = jugador["ficha"]
        break
      else :
        print("Esta casilla ya esta ocupada, Ingrese otra posición")

def calcular_ganador(tablero: list):
  tab = []
  for i in range(3):
    for j in range(3):
      tab.append(tablero[i][j])
  tablero = tab
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
    if tablero[pos1] and tablero[pos1] == tablero[pos2] == tablero[pos3]:
      return tablero[pos1]
  
  return False

while not calcular_ganador(tablero=tablero):

  agregar_pieza(jugador1)
  agregar_pieza(jugador2)
  mostrar_tablero()

print('El ganador es', calcular_ganador(tablero=tablero))


