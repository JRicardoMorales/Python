from collections import namedtuple
from collections import Counter
from datetime import datetime
import csv 

DatosVentas = namedtuple("DatosVentas", "año, comunidad, contratos, llamadas_comerciales, publicidad_redes")

def lee_datos_ventas(fichero):
    datos = []
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for año, comunidad, contratos, llamadas_comerciales, publicidad_redes in lector:
            año = int(año)
            contratos = int(contratos)
            llamadas_comerciales = int(llamadas_comerciales)
            publicidad_redes = int(publicidad_redes)

            tupla = DatosVentas(año, comunidad, contratos, llamadas_comerciales, publicidad_redes)
            datos.append(tupla)
    
    return datos


def total_contratos(datos, comunidad=None):
    numero_total_contratos = sum(r.contratos for r in datos if comunidad == None or r.comunidad == comunidad)
    return numero_total_contratos


def año_mas_contratos_por_llamadas_comunidad(datos, comunidad):
    return max(((r.año, r.contratos * 100 / r.llamadas_comerciales) for r in datos if comunidad == None or comunidad == r.comunidad), key = lambda x:x[1])


def variaciones_anuales_contratos(datos, comunidad): 
    lista = [r for r in datos if comunidad == None or r.comunidad == comunidad]
    return [(r1.año, r2.año, r2.contratos - r1.contratos) for r1, r2 in zip(lista, lista[1:])] 


def año_mas_contratos(datos):
    d = dict()
    for v in datos:
        if v.año in d:
            d[v.año] += v.contratos
        else:
            d[v.año] = v.contratos
    return max(d.items(), key = lambda x:x[1])


def agrupa_datos_por_años(datos):
    d = dict()
    for v in datos:
        d[v.año] = [0, 0, 0]
        if v.año in d:
            d[v.año][0] += v.contratos
            d[v.año][1] += v.llamadas_comerciales
            d[v.año][2] += v.publicidad_redes
        else:
            d[v.año][0] = v.contratos
            d[v.año][1] = v.llamadas_comerciales
            d[v.año][2] = v.publicidad_redes

    return d.items()

'''
El ultimo ejercicio no se puede hacer ya que no nos indica que es lo que hace la funcion de pearson

'''







