from tenis import *

###Ejercicio 6

def lee_partidos_tenis_test():
    print("El CSV contiene este numero de elementos: ", len(partidos))
    print("Los datos de los tres primeros partidos son: ", partidos[:3])

def tenista_mas_victorias_test():
    tupla = tenista_mas_victorias(partidos, None, None)
    print("Tenista con mas victorias: ", tupla) 

def n_tenistas_con_mas_errores_test():
    tupla = n_tenistas_con_mas_errores(partidos, 3)
    print("N tenistas con mas errores: ", tupla)

def num_tenistas_distintos_por_superficie_test():
    tupla = num_tenistas_distintos_por_superficie(partidos)
    print("Numero de tenistas distintos por superficie: ", tupla)

def partido_mas_errores_por_mes_test():
    tupla = partido_mas_errores_por_mes(partidos, None)
    print("Partido mas errores por mes: ", tupla)


if __name__ == '__main__':
    partidos = lee_partidos_tenis("./data/tenis.csv")
    lee_partidos_tenis_test()
    tenista_mas_victorias_test()
    n_tenistas_con_mas_errores_test()
    num_tenistas_distintos_por_superficie_test()
    partido_mas_errores_por_mes_test()