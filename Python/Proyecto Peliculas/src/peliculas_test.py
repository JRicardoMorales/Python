from peliculas import *

###Ejercicio 8

def lee_peliculas_test():
    print("El tamaño del csv es: ", len(peliculas))
    print("Los 3 primeras peliculas constan de estos datos: ", peliculas[:3])


def pelicula_mas_ganancias_test():
    tupla = pelicula_mas_ganancias(peliculas, None)
    print("La pelicula con mas ganancias con los datos dados es: ", tupla)


def media_presupuesto_por_genero_test():
    tupla = media_presupuesto_por_genero(peliculas)
    print("Media de presupuesto por genero: ", tupla)


def peliculas_por_actor_test():
    tupla = peliculas_por_actor(peliculas, 2005, 2015)
    print("Peliculas por actores: ", tupla)

def actores_mas_frecuentes_test():
    tupla = actores_mas_frecuentes(peliculas, 3 , 2005, 2015)
    print("Actores mas frecuentes: ", tupla)

def recaudacion_total_por_año_test():
    tupla = recaudacion_total_por_año(peliculas, None)
    print("Recaudacion por año: ", tupla)

def incrementos_recaudacion_por_año_test():
    tupla = incrementos_recaudacion_por_año(peliculas, None)
    print("Incrementos recaudacion por año: ", tupla)






if __name__ == '__main__':
    peliculas = lee_peliculas("./data/peliculas.csv")
    lee_peliculas_test()
    pelicula_mas_ganancias_test()
    media_presupuesto_por_genero_test()
    peliculas_por_actor_test()
    actores_mas_frecuentes_test()
    recaudacion_total_por_año_test()
    incrementos_recaudacion_por_año_test()