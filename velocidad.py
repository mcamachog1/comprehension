#lista de velocidades individuales
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

#se define la función
def vel_sobre_promedio():
    #variable que contendrá la suma de todas las medidas
    total = sum(velocidad)
    #lista vacía que contendrá todas las velocidades que estarán sobre el promedio 
    velocidades_sobre_promedio = []
        #se saca el promedio del total, dividido por la cantidad de las variables
    promedio = total / len(velocidad)
    
    #Entonces se hace otro ciclo, para verificar cuales son las que estan sobre el promedio
    #la función len es para devolver la longitud de la lista velocidad que es en la que se 
    #desea iterar

    # [fórmula for variable in iterable if condicion]
    velocidades_sobre_promedio = [index for index, velocidad_medida in enumerate(velocidad) if  velocidad_medida > promedio]

    # for index, velocidad_medida in enumerate(velocidad):
    #     if velocidad_medida > promedio:
    #         velocidades_sobre_promedio.append(index)

    # for vel_medida in range(len(velocidad)):
    #     #Condicional que establece si la velocidad medida individualmente es mayor al promedio
    #     if velocidad[vel_medida] > promedio:
    #         #entonces dicho valor se agrega a la lista de velocidades sobre el promedio
    #         velocidades_sobre_promedio.append(vel_medida)
    #         #imprime la lista con los valores respectivos 
    print(velocidades_sobre_promedio)
# Llamamos a la función
vel_sobre_promedio()

# [fórmula for variable in iterable]