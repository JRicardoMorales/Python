from baloncesto import *

def lee_partidos_test():
    print("Numero total de partidos: ", len(partidos))
    print("Los datos de 3 partidos del CSV son: ", partidos[:3])


def equipo_con_mas_faltas_test():
    tupla = equipo_con_mas_faltas(partidos, None)
    print("Equipo con mas faltas: ", tupla)


def media_puntos_por_equipo_test():
    tupla = media_puntos_por_equipo(partidos, "Copa del Rey")
    print("Media puntos por equipo en Copa del Rey: ", tupla)


def diferencia_puntos_anotados_test():
    tupla = diferencia_puntos_anotados(partidos, "Barcelona")
    print("Diferencia de puntos anotados entre partidos: ", tupla)

def victorias_por_equipo_test():
    tupla = victorias_por_equipo(partidos)
    print("Victorias por equipo: ", tupla)

def equipos_minimo_victorias_test():
    tupla = equipos_minimo_victorias(partidos, 12)
    print("Equipo minimo victorias: ", tupla)

def equipos_mas_victorias_por_año_test():
    tupla = equipos_mas_victorias_por_año(partidos, 8)
    print("Equipos mas victoria por año: ", tupla)


if __name__ == "__main__":
    partidos = lee_partidos('./data/resultados_baloncesto.csv')
    lee_partidos_test()
    equipo_con_mas_faltas_test()
    media_puntos_por_equipo_test()
    diferencia_puntos_anotados_test()
    victorias_por_equipo_test()
    equipos_minimo_victorias_test()
    equipos_mas_victorias_por_año_test()

