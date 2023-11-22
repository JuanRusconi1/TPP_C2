#Listar todas las partidas 
# Esta funcion no recibe parametros y retorna una lista con todas las partidas ya registradas
# Cada item de esta lista es un diccionario 
# Ej: {'ID': '1', 'JUGADOR1': 'alexis', 'JUGADOR2': 'Martin', 'GANADOR': 'alexis', 'RESULTADO': '102100102'}
def listar_partidas() :
  with open("./archivos/puntajes.csv", "r", encoding="utf-8") as file :
    lines = file.read().split("\n")
  keys = lines.pop(0).split(",")
  registro = [] 
  for line in lines :
    dato_partida = {}
    datos = line.split(",")
    for i in range(len(datos)) :
      dato_partida[keys[i]] = datos[i]
    registro.append(dato_partida)
  return registro

#Agregar una partida a la lista
# Esta funcion recibe como parametro un diccionario con toda la informacion de una partida
# Ej: {'JUGADOR1': 'alexis', 'JUGADOR2': 'Martin', 'GANADOR': 'alexis', 'RESULTADO': '102100102'}
# Escribe en la ultima linea la partida que se paso por parametro
# no existe la necesidad de pasar el "ID" de la partida

def agregar_partida(partida: dict) :
  datos_agregar = []
  with open("./archivos/puntajes.csv", "r", encoding="utf-8") as file :
    lines = file.read().split("\n")
    ultimo_id = lines[-1][0]

  try :
    es_numero = int(ultimo_id)
  except ValueError :
    ultimo_id = "0"
  datos_agregar.append(str(int(ultimo_id) + 1))

  for dato in partida.values() :
    datos_agregar.append(dato)
  linea = ",".join(datos_agregar)

  with open("./archivos/puntajes.csv","a", encoding="utf-8") as add_file :
    add_file.writelines(f"\n{linea}")

#Eliminar una partida de la lista
# Esta funcion recibe como parametro un numero el cual indica el numero de partida("ID") que se quiere eliminar
# Si lo en cuentra elimina esa partida y vuelve a escribir todo el archivo con todas las partidas sin contar la partida que eliminamos, retorna "True"
# Si no encuentra esa partida retorna "False"
def eliminar_partida(num_partida: int) :
  if type(num_partida) != int :
    return False
  texto_nuevo = ""
  partidas = listar_partidas()
  num_indicador = -1
  for i in range(len(partidas)) :
    if partidas[i]["ID"] == str(num_partida):
      num_indicador = i
  if num_indicador >= 0  :
    partidas.pop(num_indicador)
    lista_claves = []
    for keys in partidas[0].keys() :
      lista_claves.append(keys)
    texto_nuevo = ",".join(lista_claves)
    for item in partidas :
      datos = []
      texto_nuevo += "\n"
      for dato in item.values() :
        datos.append(dato)
      linea = ",".join(datos)
      texto_nuevo += linea
    with open("./archivos/puntajes.csv","w") as file :
      file.write(texto_nuevo)
    return True
  else :
    return False

