import sys

precios = {'Notebook': 700000,
            'Teclado': 25000,
            'Mouse': 12000,
            'Monitor': 250000,
            'Escritorio': 135000,
            'Tarjeta de Video': 1500000}

def mayores():
    """Filtra valores mayores al umbral.

    Parámetros:
    - mayores (array) -- lista que almacena las claves que pasan el filtro
    - k (str) -- clave del diccionario
    - v (int) -- valor del diccionario
    - umbral (int) -- valor para filtrar el diccionario
    """
    mayores = {k for k, v in precios.items() if umbral < v}
    print(f'{mayores}')

def menores():  #filtro para valores menores al umbral
    """Filtra valores menores al umbral.

    Parámetros:
    - mayores (array) -- lista que almacena las claves que pasan el filtro
    - k (str) -- clave del diccionario
    - v (int) -- valor del diccionario
    - umbral (int) -- valor para filtrar el diccionario
    """
    menores = {k for k, v in precios.items() if umbral > v}
    print(f'{menores}')

if len(sys.argv) == 2:    # Esperando un argumento
    umbral = int(sys.argv[1])
    mayores()
elif len(sys.argv) == 3:  # Esperando dos argumentos
    umbral, opcion = int(sys.argv[1]), sys.argv[2]
    if opcion == "mayor":
        mayores()
    elif opcion == "menor":
        menores()
    else:
        print("Opción no válida")
else:
    print("Número inválido de argumentos")
