%%writefile main.py
from operaciones_matrices import sumar_matrices, multiplicar_matrices, hadamard_matrices, kronecker
from entrada import ingresar_matriz
from menu import mostrar_menu

def ejecutar():
    while True:
        opcion = mostrar_menu()

        if opcion == 5:
          break

        print("Matriz A:")
        A = ingresar_matriz()
        print("Matriz B:")
        B = ingresar_matriz()


        try:

            if opcion == 1:
              if len(A) == len(B) and len(A[0]) == len(B[0]):
                sumar_matrices(A, B)
                print("===Resultado:===\n", sumar_matrices(A, B))
              else:
                print("Error: las matrices deben tener igual tamaño.")

            elif opcion == 2:
              if len(A[0]) == len(B):
                multiplicar_matrices(A, B)
                print("===Resultado:===\n", multiplicar_matrices(A, B))
              else:
                print("Error: columnas de A deben ser iguales a filas de B.")

            elif opcion == 3:
              if len(A) == len(B) and len(A[0]) == len(B[0]):
                hadamard_matrices(A, B)
                print("===Resultado:===\n", hadamard_matrices(A, B))
              else:
                print("Error: las matrices deben tener igual tamaño.")

            elif opcion == 4:
              kronecker(A, B)
              print("===Resultado:===\n", kronecker(A, B))

            elif opcion == 5:
              print("Saliendo del programa")
              break

        except ValueError:
            print("Opción no válida. Por favor, selecciona una opción válida.") 
