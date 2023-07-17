from collections import namedtuple
from collections import Counter
from datetime import datetime
from datetime import timedelta
from datetime import date
import csv

Reparacion = namedtuple('Reparacion', 'numero_ref,centro,fecha_entrada,fecha_reparacion, numero_serie,tipo,descripcion_problema,fecha_compra,precio_reparacion')

def lee_reparaciones(fichero):
    datos = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for numero_ref,centro,fecha_entrada,fecha_reparacion, numero_serie,tipo,descripcion_problema,fecha_compra,precio_reparacion in lector:
            fecha_entrada = datetime.strptime(fecha_entrada, "%d/%m/%Y").date()
            fecha_reparacion = datetime.strptime(fecha_reparacion, "%d/%m/%Y").date()
            fecha_compra = datetime.strptime(fecha_compra, "%d/%m/%Y").date()
            precio_reparacion = float (precio_reparacion)

            tupla = Reparacion(numero_ref,centro,fecha_entrada,fecha_reparacion, numero_serie,tipo,descripcion_problema,fecha_compra,precio_reparacion)
            datos.append(tupla)

    return datos


def calcula_recaudacion(datos, centro, tipo = None):
    return sum(v.precio_reparacion for v in datos if v.centro == centro and not esta_en_garantia(v) and tipo is None or v.tipo == tipo) 


def esta_en_garantia(r):
    return (r.fecha_compra < date(2022, 1, 1) and r.fecha_compra + timedelta(365 * 2) > r.fecha_entrada or r.fecha_compra >= date(2022, 1, 1) and r.fecha_compra + timedelta(365 * 3) > r.fecha_entrada)


def reparaciones_mas_largas(datos, año, n, centro = None):
    lista = [(r.numero_ref, dias_reparacion(r)) for r in datos if (centro is None or r.centro == centro) and r.fecha_entrada.year == año]
    lista = sorted(lista, key = lambda x:x[1], reverse = True)
    return lista [:n]

def dias_reparacion(f):
    return (f.fecha_reparacion - f.fecha_entrada).days


def centro_mas_rapido(datos, centros):
    dic = dict()
    for v in datos:
        if v.centro in centros:
            if v.centro in dic:
                dic[v.centro].append(v)
            else:
                dic[v.centro] = [v]

    res = {}
    for v, v2 in dic.items():
        suma = sum(dias_reparacion(v) for v in v2)
        res[v] = suma / len(v2)
    return min(res.items(), key = lambda x:x[1])[0]


def centros_experimentados_en(datos, keywords):
    d = agrupa_centros_por_keywords(datos, keywords)
    return {keyword:ordena_centros(lista_centros) for keyword, lista_centros in d.items()}


def agrupa_centros_por_keywords(datos, keywords):
    res = dict()
    for r in datos:
        keywords_rep = keywords_reparacion_min(r)
        for keyword in keywords:
            clave = keyword.lower()
            if clave in keywords_rep:
                if clave in res:
                    res[clave].append(r.centro)
                else:
                    res[clave] = [r.centro]

    return res


def keywords_reparacion_min(datos):
    return set(keyword.lower() for keyword in datos.descripcion_problema.split())


def ordena_centros (lista_centros):
    c = Counter(lista_centros)
    ord = sorted(c.items(), key=lambda t:t[1], reverse=True)
    return [centro for centro, _ in ord]



def dias_entre_reparaciones(datos):
    d = agrupa_reparaciones_por_num_serie(datos)
    return {num_serie:calcula_lista_dias(lista_reparaciones) for num_serie, lista_reparaciones in d.items()}

def agrupa_reparaciones_por_num_serie(datos):
    d = dict()
    for v in datos:
        if v.numero_serie in d:
            d[v.numero_serie].append(v)
        else:
            d[v.numero_serie] = [v]
    return d

def dias_funcionamiento(r):
    return (r.fecha_entrada - r.fecha_compra).days


def calcula_lista_dias(datos):
    lista_ord = sorted(datos, key=lambda t: t.fecha_entrada)
    res = [dias_funcionamiento(lista_ord[0])]
    for t1, t2 in zip(lista_ord, lista_ord[1:]):
        dias_entre_reparaciones2 = (t2.fecha_entrada - t1.fecha_reparacion).days
        res.append(dias_entre_reparaciones2)
    return res




