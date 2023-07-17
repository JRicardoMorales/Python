from collections import namedtuple
from collections import Counter
from datetime import datetime
import csv

PartidoTenis = namedtuple('PartidoTenis', 'fecha,jugador1,jugador2,superficie,resultado, errores_nf1,errores_nf2')
Set = namedtuple('Set', 'juegos_j1, juegos_j2')


###Ejercicio 1


def lee_partidos_tenis(fichero):
    datos = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for fecha,jugador1,jugador2,superficie,set1, set2, set3 , errores_nf1,errores_nf2 in lector:
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            resultado = [parsea_set(set1), parsea_set(set2), parsea_set(set3)]
            errores_nf1 = int(errores_nf1)
            errores_nf2 = int(errores_nf2)
            tupla = PartidoTenis(fecha,jugador1,jugador2,superficie,resultado, errores_nf1,errores_nf2)
            datos.append(tupla)
    
    return datos

def parsea_set(str):
    juegos = str.split("-")
    juegos_j1 = int(juegos[0])
    juegos_j2 = int(juegos[1])
    return (Set(juegos_j1, juegos_j2))


###Ejercicio 2

def tenista_mas_victorias(datos, f1 = None, f2 = None):
    dic = dict()
    for v in datos:
        if fecha_en_rango(v.fecha, f1, f2):
            if ganador(v) in dic:
                dic[ganador(v)] += 1
            else:
                dic[ganador(v)] = 1
    return max(dic, key=dic.get)



def ganador(partido):
    g = None
    resultado = partido.resultado
    if resultado[0].juegos_j1 > resultado[0].juegos_j2 and resultado[1].juegos_j1 > resultado[1].juegos_j2:
        g = partido.jugador1
    elif resultado[0].juegos_j1 < resultado[0].juegos_j2 and resultado[1].juegos_j1 < resultado[1].juegos_j2:
        g = partido.jugador2
    elif resultado[2].juegos_j1 > resultado[2].juegos_j2:
        g = partido.jugador1
    else:
        g = partido.jugador2
    
    return g

def fecha_en_rango(fecha, fecha1=None, fecha2=None):
    return (fecha1 == None or fecha1 <= fecha) and (fecha2 == None or fecha <= fecha2) 


###Ejercicio 3

def n_tenistas_con_mas_errores(datos, n = None):
    dic = dict()
    for v in datos:
        if v.jugador1 not in dic:
            dic[v.jugador1] = v.errores_nf1
        else:
            dic[v.jugador1] += v.errores_nf1
        if v.jugador2 not in dic:
            dic[v.jugador2] = v.errores_nf2
        else:
            dic[v.jugador2] += v.errores_nf2

    dic = sorted(dic.items(), key = lambda x:x[1], reverse = True)[:n]
    return dic


###Ejercicio 4

def num_tenistas_distintos_por_superficie(datos):
    dic = jugadores_por_superficie(datos)
    return {v1:len(v2) for v1, v2 in dic.items()}


def jugadores_por_superficie(datos):
    dic = dict()
    for v in datos:
        agregar_jug_sup_a_dicc(dic, v.superficie, v.jugador1)
        agregar_jug_sup_a_dicc(dic, v.superficie, v.jugador2)
    
    return dic 

def agregar_jug_sup_a_dicc(dicc, superficie, jugador):
    if superficie in dicc:
        dicc[superficie].add(jugador)
    else:
        dicc[superficie] = {jugador}


###Ejercicio 5

def partido_mas_errores_por_mes(datos, superficie = None):
    dic = dict()
    for v in datos:
        if (superficie == None or v.superficie == superficie) and v.fecha.month not in dic:
            dic[v.fecha.month] = [(v.fecha, v.jugador1, v.jugador2, v.errores_nf1 + v.errores_nf2)]
        elif (superficie == None or v.superficie == superficie) and v.fecha.month in dic:
            dic[v.fecha.month].append((v.fecha, v.jugador1, v.jugador2, v.errores_nf1 + v.errores_nf2))
    
    for v1, v2 in dic.items():
        dic[v1] = max(v2, key = lambda x:x[3])
    
    for v1, v2 in dic.items():
        dic[v1] = (v2[0], v2[1], v2[2])
    
    dic = sorted(dic.items())

    return dic
        





