from collections import namedtuple
from collections import defaultdict
from collections import Counter
from datetime import datetime
import csv

Pelicula = namedtuple("Pelicula", "fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto")

###Ejercicio 1


def lee_peliculas(fichero):
    datos = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ";")
        next(lector)
        for fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto in lector:
            fecha_estreno = datetime.strptime(fecha_estreno, "%d/%m/%Y").date()
            generos = parsea_listas(generos)
            duracion = int(duracion)
            presupuesto = int(presupuesto)
            recaudacion = int(recaudacion)
            reparto = parsea_listas(reparto)

            tupla = Pelicula(fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto)
            datos.append(tupla)
    
    return datos

def parsea_listas(lista_str):
    trozos = lista_str.split(",")
    return [t.strip() for t in trozos]


###Ejercicio 2

def pelicula_mas_ganancias(datos, genero = None):
    lista = list()
    for v in datos:
        if genero in v.generos or genero == None:
            lista.append(v)
    maximo = max(lista, key = lambda x:x.recaudacion - x.presupuesto)
    return (maximo.titulo, maximo.recaudacion - maximo.presupuesto)


###Ejercicio 3

def media_presupuesto_por_genero(datos):
    dic = dict()
    for v in datos:
        for x in v.generos:
            if x in dic:
                dic[x].append(v.presupuesto)
            else:
                dic[x] = [v.presupuesto]

    res = {}
    for v1, v2 in dic.items():
        res[v1] = sum(v2) / len(v2)
    
    return res


###Ejercicio 4
    
def peliculas_por_actor(datos, año_inicial = None, año_final = None):
    dic = dict()
    for v in datos:
        for x in v.reparto:
            if x in dic and esta_en_fecha(v.fecha_estreno.year, año_inicial, año_final):
                dic[x] += 1
            elif x not in dic and esta_en_fecha(v.fecha_estreno.year, año_inicial, año_final):
                dic[x] = 1

    return dic


def esta_en_fecha(fecha, f1, f2):
    if f1 == None and f2 == None:
        res = True
    elif f1 == None and fecha <= f2:
        res = True
    elif f2 == None and fecha >= f1:
        res = True
    elif f1 != None and f2 != None and f1 <= fecha <= f2:
        res = True
    else:
        res = False
    return res


###Ejercicio 5

def actores_mas_frecuentes(datos, n , año_inicial = None, año_final = None):
    dic = peliculas_por_actor(datos, año_inicial, año_final)
    mas_frecuentes = sorted(dic.items(), key=lambda t: t[1], reverse =True)[:n]
    return sorted(v1 for v1, v2 in mas_frecuentes)


###Ejercicio 6

def recaudacion_total_por_año(datos, generos = None):
    dic = defaultdict(int)
    for v in datos:
        if generos is None or len(generos.intersection(v.generos)) > 0:
            dic[v.fecha_estreno.year] += v.recaudacion
    return dic


###Ejercicio 7

def incrementos_recaudacion_por_año(datos, generos = None):
    dic = recaudacion_total_por_año(datos, generos)
    recaudaciones = [v2 for v1, v2 in sorted(dic.items(), key = lambda x:x[0])]
    return [r2 - r1 for r1, r2 in zip(recaudaciones, recaudaciones[1:])]





























