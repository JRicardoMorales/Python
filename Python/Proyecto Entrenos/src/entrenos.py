from collections import namedtuple
from datetime import datetime
from collections import Counter
import csv

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(fichero):
    datos = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M").date()
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = parse_bool(compartido)
            tupla = Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            datos.append(tupla)
    
    return datos


def parse_bool(compartido):
    if compartido == 'S':
        return True
    else:
        return False
    

def porcentaje_calorias_por_tipo(datos, tipos):
    dic = dict()
    for v in datos:
        if v.tipo in tipos:
            if v.tipo in dic:
                dic[v.tipo] += v.calorias
            else:
                dic[v.tipo] = v.calorias
    
    total = sum(v.calorias for v in datos)
    for v, v2 in dic.items():
        dic[v] = v2 * 100 / total
    
    return dic

def año_mayor_distancia_media(datos, c, d):
    dic = dict()
    for v in datos:
        if (v.compartido == c or c == None) and v.distancia > d:
            if v.fechahora.year in dic:
                dic[v.fechahora.year].append(v.distancia)
            else:
                dic[v.fechahora.year] = [v.distancia]
    
    for v, v2 in dic.items():
        dic[v] = sum(v2) / len(v2)
    
    return max(dic, key = dic.get)


def entrenos_mas_repetidos(datos, f1, f2):
    dic = dict()
    for v in datos:
        if esta_en_fecha(v, f1, f2):
            if v.ubicacion in dic:
                dic[v.ubicacion].append(v.tipo)
            else:
                dic[v.ubicacion] = [v.tipo]
    
    for v, v2 in dic.items():
        dic[v] = Counter(v2).most_common()[0][0]
    
    return dic




def esta_en_fecha(r, f1, f2):
    if f1 == None and f2 == None:
        return True
    elif f1 != None:
        return r > f1
    elif f2 != None:
        return r < f2
    else:
        return f1 < r < f2
    


def acumular_por_años(datos):
    datos.sort(key = lambda x:x.fechahora.year)
    dic = dict()
    for v in datos:
        if v.fechahora.year in dic:
            dic[v.fechahora.year] += v.distancia
        else:
            dic[v.fechahora.year] = v.distancia

    return dic

def incrementos_anuales_distancia(datos):
    d = acumular_por_años(datos)
    año_min = min(d)
    año_max = max(d)
    años = [a for a in range(año_min, año_max+1)]
    res = []
    for año1, año2 in zip(años, años[1:]):
        inc = d.get(año2, 0) - d.get(año1, 0)
        res.append(inc)
    
    return res















    

