from partidas import *

##Ejercicio 7

def lee_partidas_test():
    print("Partidas totales que contiene el csv: ", len(games))
    print("Las tres primeras partidas son: ", games[:3])

def victoria_mas_rapida_test():
    tupla = victoria_mas_rapida(games)
    print("La partida mas rapidas del csv fue entre estos dos jugadores y duró este tiempo: ", tupla)

def top_ratio_media_personajes_test():
    tupla = top_ratio_media_personajes(games, 3)
    print("Top 3 personajes con menor ratio: ", tupla)

def enemigos_mas_debiles_test():
    tupla = enemigos_mas_debiles(games, "Ken")
    print("Enemigos mas debiles para Ken: ", tupla)

def movimientos_comunes_test():
    tupla = movimientos_comunes(games, "Ryu", "Ken")
    print("Movimientos comunes a Ryu y Ken:", tupla)

def dia_mas_combo_finish_test():
    tupla = dia_mas_combo_finish(games)
    print("Dia de la semana con mas combos finales: ", tupla)


if __name__ == '__main__':
    games = lee_partidas("./data/games.csv")
    lee_partidas_test()
    victoria_mas_rapida_test()
    top_ratio_media_personajes_test()
    enemigos_mas_debiles_test()
    movimientos_comunes_test()
    dia_mas_combo_finish_test()