#Importar librería sys 
import sys

#diccionario de productos y precios
precios = {'Notebook': 700000,
 'Teclado': 25000,
 'Mouse': 12000,
 'Monitor': 250000,
 'Escritorio': 135000,
 'Tarjeta de Video': 1500000}

# #Se define la función que filtrará los productos mayores a el umbral ingresado, dicho 
# #umbral será el páramtro a recibir.
# def filtro_mayor_a(umbral):
#     #utilizo un diccionario vacío para almacenar los productos filtrados
#     productos_mayor_a = {}
#     # utilizo un ciclo for que recorre el diccionario 
#     for producto, precio in precios.items():
#         #si el valor es mayor al umbral
#         if precio > umbral:
#             #si se cumple, se añade el producto al diccionario
#             productos_mayor_a[producto] = precio
#             #retorna los productos que cumplen la condición
#     return productos_mayor_a


# #Se define la función que será la que hará la diferencia entre mayor y menor de los precios en los productos
# #recibe por parametros el umbral y la condición
# def filtro_mayor_menor(umbral, condicion):
#     producto_valido = {}
#     #si la condición es igual a "mayor"
#     if condicion =='mayor':
#         #entonces se llama a la función
#        producto_valido = filtro_mayor_a(umbral)
#     else:
#         #si es menor simplemente se valida
#         for producto, precio in precios.items():
#             if precio < umbral:
#             #si es menor se agrega por el precio a la lista de productos válidos 
#                 producto_valido[producto] = precio
#                 #se retornan los productos validos
#     return producto_valido

def filtrar(diccionario, umbral, condicion='mayor'):
    if condicion == 'mayor':
        productos = [key for key, value in diccionario.items() if value > umbral]
    elif condicion == 'menor':
        productos = [key for key, value in diccionario.items() if value < umbral]
    else:
        print('Lo sentimos, no es una operación válida')
    return productos

def filtro(cant_argumentos):
    #Si la cantidad de argumento son tres
    if cant_argumentos == 3:
        #Donde el umbral es el primero
        umbral = int(sys.argv[1])
        #la condición es el segundo
        condicion = sys.argv[2]
        #si la condicion es mayor o menor 
        if condicion in {'menor', 'mayor'}:
            #se llama la función filtro_mayor_menor
            productos_validos = filtrar(precios,umbral,condicion)
            #imprime los productos que cumplen la condición 
            print(f'Los productos {condicion}es al umbral son: {", ".join(productos_validos)}')
        else:
            #si no, no lo toma como valido
            print('Lo sentimos, no es una operación válida')
            #en cambio si la cantidad de argumentos son dos
    elif cant_argumentos== 2:
        umbral = int(sys.argv[1])
        #se llama a la función que filtra los productos mayores al umbral y los imprime
        productos_validos = filtrar(precios,umbral)
        print(f'Los productos mayores al umbral son: {", ".join(productos_validos)}')

#Se llama a la funcion , donde len determina la cantidad de argumentos que se pasan para hacer una cosa u otra. 
filtro(len(sys.argv))