from collections import namedtuple
from datetime import datetime
from collections import Counter
import csv

Partida = namedtuple("Partida", "pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2, movimiento_final, combo_finish, ganador")



###Ejercicio 1

def lee_partidas(fichero):
    datos = []
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2, movimiento_final, combo_finish, ganador in lector:
            puntuacion = int(puntuacion)
            tiempo = float(tiempo)
            fecha_hora = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M:%S")
            golpes_pj1 = parsea_lista(golpes_pj1)
            golpes_pj2 = parsea_lista(golpes_pj2)
            combo_finish = parse_bool(combo_finish)

            tupla = Partida(pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2, movimiento_final, combo_finish, ganador)
            datos.append(tupla)
    
    return datos

def parse_bool(combo_finish):
    return combo_finish == "1"

def parsea_lista(lista_str):
    lista_str = lista_str.replace("[", " ")
    lista_str = lista_str.replace("]", " ")
    trozos = lista_str.split(",")
    return [t.strip() for t in trozos]



###Ejercicio 2

def victoria_mas_rapida(datos):
    res = None
    for p in datos:
        if res == None or res.tiempo > p.tiempo:
            res = p
    return res.pj1, res.pj2, res.tiempo

###Ejercicio 3

def top_ratio_media_personajes(datos, n):
    lista = []
    dic_auxiliar = media_ratio(datos)
    dic = sorted(dic_auxiliar.items(), key = lambda x:x[1])[:n]
    for v1, v2 in dic:
        lista.append(v1)
    return lista


def media_ratio(datos):
    dic = dict()
    for v in datos:
        if v.ganador in dic:
            dic[v.ganador].append(v.puntuacion/v.tiempo)
        else:
            dic[v.ganador] = [v.puntuacion/v.tiempo]
    
    for v1, v2 in dic.items():
        dic[v1] = sum(v2) / len(v2)

    return dic


###Ejercicio 4

def enemigos_mas_debiles(datos, personaje):
    dic = dict()
    lista = list()
    for v in datos:
        if v.pj1 == v.ganador and v.ganador == personaje and v.pj2 not in dic:
            dic[v.pj2] = 1
        elif v.pj1 == v.ganador and v.ganador == personaje and v.pj2 in dic:
            dic[v.pj2] += 1
        if v.pj2 == v.ganador and v.ganador == personaje and v.pj1 not in dic:
            dic[v.pj1] = 1
        elif v.pj2 == v.ganador and v.ganador == personaje and v.pj1 in dic:
            dic[v.pj1] += 1
    maximo = max(dic.items(), key = lambda x:x[1])
    for v1, v2 in dic.items():
        if v2 == maximo[1]:
            lista.append(v1)
    return (lista, maximo[1])


###Ejercicio 5

def movimientos_comunes(datos, personaje1, personaje2):
    mov1 = movimientos_ambos_personajes(datos, personaje1)
    mov2 = movimientos_ambos_personajes(datos, personaje2)
    return list(mov1 and mov2)



def movimientos_ambos_personajes(datos, personaje):
    res = set()
    for v in datos:
        if v.pj1 == personaje:
            res |= set(v.golpes_pj1)
        if v.pj2 == personaje:
            res |= set(v.golpes_pj2)
    return res
        

###Ejercicio 6

def dia_mas_combo_finish(datos):
    dic = contar_dias(datos)
    dic2 = max(dic.items(), key = lambda x:x[1])
    return dic2[0]


def contar_dias(datos):
    res = dict()
    for v in datos:
        if v.combo_finish:
            dia = v.fecha_hora.isoweekday()
            clave = get_nombre_del_dia(dia)
            if clave not in res:
                res[clave] = 1
            else:
                res[clave] += 1
    return res


def get_nombre_del_dia(str):
    if str == 0:
        return "Lunes"
    elif str == 1:
        return "Martes"
    elif str == 2:
        return "Miércoles"
    elif str == 3:
        return "Jueves"
    elif str == 4:
        return "Viernes"
    elif str == 5:
        return "Sábado"
    elif str == 6:
        return "Domingo"




