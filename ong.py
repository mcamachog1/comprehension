#Se define la funcion que calculará el factorial
def factorial(factorial):
    #Si el total es inicializada en 1, porque el factorial de 0 es 1 
    resultado_factorial = 1
    # se usa un ciclo para multiplicar todos los números desde 1 hasta el número dado que es cinco 
    for factorial in range(1, factorial + 1):
        #se acumula el resultado de la secuencia en la variable total
        resultado_factorial *= factorial
        #retorna el resultado
    return resultado_factorial

#Se define la funcion que calculará la productoria
def productoria(lista_numeros = []):
    #Se inicializa en uno
    resultado_productoria = 1
    #se usa un ciclo para iterar por cada numero en la lista numero 
    for productoria in lista_numeros:
        #se acumula el resultado de la iteración de cada numero
        resultado_productoria *= productoria
        #retorna el resultado
    return resultado_productoria

#Se define la función calcular mediante el uso de **kwargs, para pasarle los parametros en cualquier orden
def calcular(**kwargs):
    for key, value in kwargs.items():
        if 'fact' in key:
            print(f'El factorial de {value} es {factorial(value)}')
        elif 'prod' in key:
            print(f'La productoria de {value} es {productoria(value)}')
        
#Se llama la función calcular
#calcular(fact_1 = 5, prod_1 = [4,6,7,4,3],fact_2 = 6)
calcular(fact_1 = 5, prod_1 =  [4, 6, 7, 4, 3], fact_2 = 6)