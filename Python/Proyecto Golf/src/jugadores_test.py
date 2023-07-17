from jugadores import *
from datetime import date

def lee_jugadores_test():
    print("El numero de jugadores contenidos en el dataset es: ", len(jugadores))
    print("Los datos de los tres primeros jugadores son: ", jugadores[:3])

def mejores_jugadores_test():
    tupla = mejores_jugadores(jugadores, 1969, 4)
    print("Mejores jugadores con estos parametros: ", tupla)

def jugadores_por_golpes_test():
    tupla = jugadores_por_golpes(jugadores)
    print("Jugadores por golpes:", tupla)

def promedio_ultimos_resultados_test():
    tupla = promedio_ultimos_resultados(jugadores, date(2020, 3, 1), date(2020, 5, 31))
    print("Promedio ultimos resultados: ", tupla)

def jugador_menor_handicap_por_federacion_test():
    tupla = jugador_menor_handicap_por_federacion(jugadores)
    print("Jugador menor handicap por federacion:", tupla)

def comparativa_de_mejores_resultados_segun_handicap_test():
    tupla = comparativa_de_mejores_resultados_segun_handicap(jugadores)
    print("Comparativa mejores resultados segun handicap: ", tupla)


if __name__ == '__main__':
    jugadores = lee_jugadores("./data/jugadores.csv")
    lee_jugadores_test()
    mejores_jugadores_test()
    jugadores_por_golpes_test()
    promedio_ultimos_resultados_test()
    jugador_menor_handicap_por_federacion_test()
    comparativa_de_mejores_resultados_segun_handicap_test()
