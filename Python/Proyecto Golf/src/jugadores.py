from collections import namedtuple
from datetime import datetime
from collections import Counter
from datetime import date
import csv

Jugador = namedtuple('Jugador', 'ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados')

def lee_jugadores(fichero):
    datos = []
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados in lector:
            fecha_ncto = datetime.strptime(fecha_ncto, "%d/%m/%Y").date()
            handicap = float(handicap)
            fec_hor_act = datetime.strptime(fec_hor_act, "%d/%m/%Y %H:%M:%S").date()
            senior = parsea_bool(senior)
            resultados = parsea_resultados(resultados)

            tupla = Jugador(ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados)
            datos.append(tupla)

    return datos


def parsea_bool(senior):
    if senior == 'S':
        res = True
    else:
        res = False
    return res

def parsea_resultados(resultados):
    return [int (resultado) for resultado in resultados.split(",")]


def mejores_jugadores(datos, año, n):
    lista = [(r.licencia, r.ape_nom, r.handicap) for r in datos if r.fecha_ncto.year == año]
    lista = sorted(lista, key = lambda x:x[2])
    return lista[:n]


def jugadores_por_golpes(datos):
    d = dict()
    for v in datos:
        for j in v.resultados:
            if j in d:
                d[j].add(v.licencia)
            else:
                d[j] = {v.licencia}
   
    return d


def promedio_ultimos_resultados(datos, f1 = None, f2 = None):
    return [(j.licencia, promedio_golpes(j.resultados)) for j in datos if j.senior == True and esta_en_fecha(j, f1, f2)]

def promedio_golpes(resultados):
    res = None
    if len(resultados) > 0:
        res = sum(resultados) / len(resultados)
    return res



def esta_en_fecha(f, f1, f2):
    return (f1 == None or f1 <= f.fec_hor_act) and (f2 == None or f.fec_hor_act <= f2)


def jugador_menor_handicap_por_federacion(datos):
    d = agrupa_por_federacion(datos)
    return {federacion: mejor_jugador(lista_jugadores) for federacion, lista_jugadores in d.items()}

def agrupa_por_federacion(datos):
    res = dict()
    for j in datos:
        if j.federacion in res:
            res[j.federacion].append(j)
        else:
            res[j.federacion]= [j]
    return res

def mejor_jugador (lista_jugadores):
    return min(((j.ape_nom, j.handicap) for j in lista_jugadores), key=lambda t:t[1])




def comparativa_de_mejores_resultados_segun_handicap(datos):
    d_promedios = promedios_por_handicap(datos)
    return diferencias_promedios(d_promedios)

def promedios_por_handicap(datos):
    d = dict()
    for j in datos:
        clave = j.handicap
        if clave in d:
            d[clave].append(min(j.resultados))
        else:
            d[clave]=[min(j.resultados)]

    return {handicap: media_resultados(mejores_resultados) for handicap, mejores_resultados in d.items()}


def media_resultados(resultados):
    return sum(resultados) / len(resultados)

def diferencias_promedios(d_promedios):
    promedios_ord=sorted(d_promedios.items())
    return [ (f"{t1[0]} vs {t2[0]}", t1[1] - t2[1]) for t1, t2 in zip(promedios_ord, promedios_ord[1:])]








