from artistas import *

###Test de los Ejercicios 0, 1, 2, 3, 4, 5 y 6

def lee_artistas_test():
    print("El numero de elementos del csv es: ", len(artistas))
    print("Los datos de los primeros 3 artistas son: ", artistas[:3])

def actuaciones_artistas_test():
    tupla = actuaciones_artistas(artistas, "Dalila")
    print("Actuaciones del artista pasado por parametro: ", tupla)

def conciertos_hora_test():
    tupla = conciertos_hora(artistas, datetime(2020, 3, 4, 20, 0, 1).time())
    print("Conciertos a la hora dada por parametro: ", tupla)

def primer_concierto_fecha_test():
    tupla = primer_concierto_fecha(artistas, datetime(2021, 7, 1, 0, 0, 0).date())
    print("Primer concierto a partir de esta fecha", tupla)

def artista_en_mes_y_año_test():
    tupla = artista_en_mes_y_año(artistas, 7, 2021)
    print("Concierto de artista en mes y año indicados: ", tupla)

def artista_mas_recaudacion_total_test():
    tupla = artista_mas_recaudacion_total(artistas)
    print("El artista con mas recaudaciones es: ", tupla)

def agenda_mensual_precio_aforo_test():
    tupla = agenda_mensual_precio_aforo(artistas)
    print("Media de precio y aforo total por mes de los conciertos del CSV: ", tupla)

if __name__ == '__main__':
    artistas = lee_artistas("./data/artistas.csv")
    lee_artistas_test()
    actuaciones_artistas_test()
    conciertos_hora_test()
    primer_concierto_fecha_test()
    artista_en_mes_y_año_test()
    artista_mas_recaudacion_total_test()
    agenda_mensual_precio_aforo_test()