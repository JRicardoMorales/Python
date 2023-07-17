from entrenos import *

def lee_entrenos_test():
    print("El numero total de entrenos del CSV es: ", len(entrenos))
    print("Los primeros entrenos son: ", entrenos[:3])

def porcentaje_calorias_por_tipo_test():
    tupla = porcentaje_calorias_por_tipo(entrenos, "Tenis, Remo")
    print("Porcentaje de calorias de los tipos seleccionados respecto a las calorias totales: ", tupla)

def año_mayor_distancia_media_test():
    tupla = año_mayor_distancia_media(entrenos, None, 15)
    print("Año mayor distancia media con los parametros dados:", tupla)


def entrenos_mas_repetidos_test():
    tupla = entrenos_mas_repetidos(entrenos, None, None)
    print("Entrenos mas repetidos:", tupla)


def incrementos_anuales_distancia_test():
    tupla = incrementos_anuales_distancia(entrenos)
    print("Incrementos anuales de distancia: ", tupla)

if __name__ == '__main__':
    entrenos = lee_entrenos('./data/entrenos.csv')
    lee_entrenos_test()
    porcentaje_calorias_por_tipo_test()
    año_mayor_distancia_media_test()
    entrenos_mas_repetidos_test()
    incrementos_anuales_distancia_test()