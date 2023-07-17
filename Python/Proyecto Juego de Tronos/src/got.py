from collections import namedtuple
from collections import Counter
from datetime import datetime
import csv

BatallaGOT = namedtuple('BatallaGOT', 'nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados')


###Ejercicio 1

def lee_batallas(fichero):
    datos = []
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ";")
        next(lector)
        for nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados in lector:
            gana_atacante = gana_atacante == "win"
            muertes_principales = muertes_principales == "1"
            comandantes_atacantes = parsea_comandantes(comandantes_atacantes)
            comandantes_atacados = parsea_comandantes(comandantes_atacados)
            num_atacantes = parsea_entero(num_atacantes)
            num_atacados = parsea_entero(num_atacados)

            tupla = BatallaGOT(nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados)
            datos.append(tupla)

    return datos


def parsea_entero(str):
    if str == "":
        return None
    else:
        return int(str)


def parsea_comandantes(str):
    if str == "":
        return []
    else:
        str = str.split(",")
        return [t.strip() for t in str]
    

###Ejercicio 2

def reyes_mayor_menor_ejercito(datos):
    dic = dict()
    for v in datos:
        if v.num_atacados != None and v.num_atacantes != None:
            if v.rey_atacado in dic:
                dic[v.rey_atacado] += v.num_atacados
            else:
                dic[v.rey_atacado] = v.num_atacados
            if v.rey_atacante in dic:
                dic[v.rey_atacante] += v.num_atacantes
            else:
                dic[v.rey_atacante] = v.num_atacantes

    maximo = max(dic.items(), key = lambda x:x[1])
    minimo = min(dic.items(), key = lambda x:x[1])

    return (maximo[0], minimo[0])


###Ejercicio 3

def batallas_mas_comandantes(datos, regiones = None, n = None):
    lista = list()
    for v in datos:
        if regiones == None or v.region in regiones:
            lista.append((v.nombre, len(v.comandantes_atacantes) + len(v.comandantes_atacados)))
    
    lista = sorted(lista, key = lambda x:x[1], reverse = True)
    return lista[:n]


###Ejercicio 4

def rey_mas_victorias(datos, rol = "ambos"):
    dic = dict()
    dic2 = dict()
    dic3 = dict()
    for v in datos:
            if v.gana_atacante and v.rey_atacante not in dic:
                dic[v.rey_atacante] = 1
            elif v.gana_atacante and v.rey_atacante in dic:
                dic[v.rey_atacante] += 1
            if not v.gana_atacante and v.rey_atacado not in dic:
                dic[v.rey_atacado] = 1
            elif not v.gana_atacante and v.rey_atacado in dic:
                dic[v.rey_atacado] += 1

            if v.gana_atacante and v.rey_atacante not in dic2:
                dic2[v.rey_atacante] = 1
            elif v.gana_atacante and v.rey_atacante in dic2:
                dic2[v.rey_atacante] += 1
        
            if not v.gana_atacante and v.rey_atacado not in dic3:
                dic3[v.rey_atacado] = 1
            elif not v.gana_atacante and v.rey_atacado in dic3:
                dic3[v.rey_atacado] += 1

    maximo = max(dic.items(), key = lambda x:x[1])
    maximo2 = max(dic2.items(), key = lambda x:x[1])
    maximo3 = max(dic3.items(), key = lambda x:x[1])

    if rol == "ambos":
        return maximo[0]
    elif rol == "atacante":
        return maximo2[0]
    elif rol == "atacado":
        return maximo3[0]
    else:
        return None
    

###Ejercicio 5

def rey_mas_victorias_por_region(datos, rol = "ambos"):
    res = {}
    for v in datos:
        if v.region in res:
            res[v.region].append(v)
        else:
            res[v.region] = [v]

        for v1, v2 in res.items():
            res[v1] = rey_mas_victorias(v2, rol)

    return res



    








