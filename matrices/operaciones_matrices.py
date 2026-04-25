%%writefile operaciones_matrices.py

def sumar_matrices(A, B):

  filas = len(A)
  columnas = len(A[0])

  if filas != len(B) or columnas != len(B[0]):
    return "Error: las matrices no tienen las mismas dimensiones."

  else:
    try:
      resultado = []
      for i in range(filas):
        fila = []
        for j in range(columnas):
          fila.append(float(A[i][j]) + float(B[i][j]))
        resultado.append(fila)
      return resultado

    except ValueError:
      return "Debe ingresar solo números"

def multiplicar_matrices(A, B):

  filas_A = len(A)
  columnas_A = len(A[0])
  filas_B = len(B)
  columnas_B = len(B[0])

  if columnas_A != filas_B:
    return "Error: las matrices no se pueden multiplicar."

  resultado = []
  for i in range(filas_A):
    fila = []
    for j in range(columnas_B):
      suma = 0
      for k in range(columnas_A):
        suma += A[i][k]*B[k][j]
      fila.append(suma)
    resultado.append(fila)

  return resultado

def hadamard_matrices(A, B):
  filas = len(A)
  columnas = len(A[0])

  if filas != len(B) or columnas != len(B[0]):
    return "Error: las matrices no tienen las mismas dimensiones."

  else:
    resultado = []
    for i in range(filas):
      fila = []
      for j in range(columnas):
        fila.append(A[i][j]*B[i][j])
      resultado.append(fila)

    return resultado

def kronecker(A, B):
  filas_A = len(A)
  columnas_A = len(A[0])
  filas_B = len(B)
  columnas_B = len(B[0])

  resultado = []

  for  i in range(filas_A):
    for k in range(filas_B):
      fila = []
      for j in range(columnas_A):
        for l in range(columnas_B):
          fila.append(A[i][j]*B[k][l])
      resultado.append(fila)
  return resultado 
