from collections import namedtuple
from datetime import datetime
from collections import Counter
import csv
from collections import defaultdict


PartidoBasket = namedtuple('PartidoBasket','fecha, equipo1, equipo2, competicion, puntos_eq1, puntos_eq2, faltas_eq1, faltas_eq2')

def parsea_y_suma_resultados(cadena):
    puntos_eq1, puntos_eq2 = 0, 0
    for p in cadena.split("*"):
        eq1, eq2 = p.split("-")
        puntos_eq1 += int(eq1)
        puntos_eq2 += int(eq2)

    return puntos_eq1, puntos_eq2


def lee_partidos(fichero):
    datos = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        for fecha, equipo1, equipo2, competicion, resultados, faltas_eq1, faltas_eq2 in lector:
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            puntos_eq1 = parsea_y_suma_resultados(resultados)[0]
            puntos_eq2 = parsea_y_suma_resultados(resultados)[1]
            faltas_eq1 = int(faltas_eq1)
            faltas_eq2 = int(faltas_eq2)

            tupla = PartidoBasket(fecha, equipo1, equipo2, competicion, puntos_eq1, puntos_eq2, faltas_eq1, faltas_eq2)
            datos.append(tupla)

    return datos

def equipo_con_mas_faltas(datos, equipos = None):
    dicc = defaultdict(int)
    for p in datos:
        if equipos is None or p.equipo1 in equipos:
            dicc[p.equipo1] += p.faltas_eq1
        if equipos is None or p.equipo2 in equipos:
            dicc[p.equipo2] += p.faltas_eq2
    
    return max(dicc.items(), key=lambda x: x[1])


def media_puntos_por_equipo(datos, competicion):
    dicc_puntos = defaultdict(list)
    for p in datos:
        if p.competicion == competicion:
            dicc_puntos[p.equipo1].append(p.puntos_eq1)
            dicc_puntos[p.equipo2].append(p.puntos_eq2)
    res = {}
    for equipo, puntos in dicc_puntos.items():
        res[equipo] = sum(puntos) / len(puntos)

    return res


def diferencia_puntos_anotados(datos, equipo):
    resultados_equipo = []
    for p in datos:
        if p.equipo1 == equipo:
            resultados_equipo.append((p.fecha, p.puntos_eq1))
        elif p.equipo2 == equipo:
            resultados_equipo.append((p.fecha, p.puntos_eq2))
            resultados_equipo = sorted(resultados_equipo)

    return [p2[1] - p1[1] for p1, p2 in zip(resultados_equipo, resultados_equipo[1:])]


def victorias_por_equipo(datos):
    dicc_cont = Counter(p.equipo1 for p in datos if p.puntos_eq1 > p.puntos_eq2) + Counter(p.equipo2 for p in datos if p.puntos_eq2 > p.puntos_eq1)
    return dicc_cont   


def equipos_minimo_victorias(datos, n):
    dicc = victorias_por_equipo(datos)
    return sorted((equipo for equipo, victorias in dicc.items() if victorias >= n), key=lambda t:t[1])


def equipos_mas_victorias_por_año(lista_partidos, n):
    partidos_por_año = defaultdict(list)
    for p in lista_partidos:
        partidos_por_año[p.fecha.year].append(p)
    res = {}
    for año, partidos_año in partidos_por_año.items():
        res[año] = equipos_minimo_victorias(partidos_año, n)

    return res












