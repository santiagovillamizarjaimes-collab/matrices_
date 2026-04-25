%%writefile entrada.py

def ingresar_matriz():

  filas = int(input("Ingrese el número de filas: "))
  columnas = int(input("Ingrese el número de columnas: "))

  matriz = []

  for i in range(filas):
    while True:
      fila = list(map(float, input(f"Ingrese la fila {i+1} separada por espacios").split()))

      if len(fila) != columnas:
        print(f"Error: debe ingresar exactamente {columnas} valores")
      else:
        matriz.append(fila)
        break
  return matriz 
