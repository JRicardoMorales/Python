from got import *

###Test de los Ejercicios 1, 2, 3, 4 y 5

def lee_batallas_test():
    print("El CSV contiene ", len(batallas), " elementos")
    print("Los datos de las 3 primeras batallas son: ", batallas[:3])

def reyes_mayor_menor_ejercito_test():
    tupla = reyes_mayor_menor_ejercito(batallas)
    print("Reyes con mayor y menor ejercito: ", tupla)

def batallas_mas_comandantes_test():
    tupla = batallas_mas_comandantes(batallas, "The North, The Riverlands", 4)
    print("Batallas con mas comandantes: ", tupla)

def rey_mas_victorias_test():
    tupla = rey_mas_victorias(batallas, "ambos")
    print("Rey mas victorias dependiendo del rol: ", tupla)

def rey_mas_victorias_por_region_test():
    tupla = rey_mas_victorias_por_region(batallas, "ambos")
    print("Rey mas victorias por region: ", tupla)


if __name__ == '__main__':
    batallas = lee_batallas("./data/battles.csv")
    lee_batallas_test()
    reyes_mayor_menor_ejercito_test()
    batallas_mas_comandantes_test()
    rey_mas_victorias_test()
    ###rey_mas_victorias_por_region_test()