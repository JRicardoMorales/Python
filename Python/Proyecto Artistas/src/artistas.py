from collections import namedtuple
from datetime import datetime 
from collections import Counter
import csv

Concierto = namedtuple("Concierto", "artista, artistas_invitados, fecha, hora_apertura, hora_concierto, precio, aforo, admite_menores")

###Ejercicio 0 (Lectura)

def lee_artistas(fichero):
    datos = []
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter= ";")
        for artista, artistas_invitados, fecha, hora_apertura, hora_concierto, precio, aforo, admite_menores in lector:
            artistas_invitados = parsea_artistas(artistas_invitados)
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            hora_apertura = datetime.strptime(hora_apertura, "%H:%M" ).time()
            hora_concierto = datetime.strptime(hora_concierto, "%H:%M" ).time()
            precio = float(precio)
            aforo = int(aforo)
            admite_menores = parsea_bool(admite_menores)
            
            tupla = Concierto(artista, artistas_invitados, fecha, hora_apertura, hora_concierto, precio, aforo, admite_menores)
            datos.append(tupla)

    return datos


def parsea_artistas(str):
    str = str.split(",")
    return [v.strip() for v in str]

def parsea_bool(str):
    if str == "True":
        return True
    else:
        return False


###Ejercicio 1

def actuaciones_artistas(datos, artistas):
    lista = list()
    for v in datos:
        if v.artista in artistas or artistas in v.artistas_invitados:
            lista.append(v)
        
    return lista


###Ejercicio 2

def conciertos_hora(datos, hora = None):
    lista = list()
    for v in datos:
        if (hora == None or hora >= v.hora_concierto) and v.admite_menores == True:
            lista.append((v.artista, v.artistas_invitados, v.fecha))

    lista = sorted(lista, key = lambda x:x[2])

    return lista


###Ejercicio 3

def primer_concierto_fecha(datos, fecha = None):
    lista = list()
    for v in datos:
         if fecha == None or fecha <= v.fecha:
             lista.append((v.artista, v.fecha, v.hora_apertura))
    minimo = min(lista, key = lambda x:x[2])

    return (minimo[0], minimo[1])


###Ejercicio 4

def artista_en_mes_y_año(datos, mes, año):
    lista = list()
    for v in sorted(datos, key=lambda x:x.fecha):
        if v.fecha.month == mes and v.fecha.year == año:
            if v.artista not in lista:
                lista.append(v.artista)
            for x in v.artistas_invitados:
                if x not in lista:
                    lista.append(x)
    return lista


###Ejercicio 5

def artista_mas_recaudacion_total(datos):
    artistas = set()
    for v in datos:
        artistas.add(v.artista)
        for i in v.artistas_invitados:
            artistas.add(i)
    pagos = list()
    for a in artistas:
        pagos.append((a, calculo_recaudacion(datos, a)))
    
    return max(pagos, key = lambda t:t[1])



def calculo_recaudacion(datos, a):
    pago = 0
    for v in datos:
        cantidad = (v.precio * v.aforo) / 3
        if v.artista == a:
            pago += cantidad
        elif a in v.artistas_invitados:
            pago += cantidad / len(v.artistas_invitados)
    return pago


###Ejercicio 6

def agenda_mensual_precio_aforo(datos):
    dicc_precio = dict()
    dicc_aforo = dict()
    dicc_num = dict()
    for v in datos:
        clave = str(v.fecha.month) + '-' + str(v.fecha.year)
        if clave in dicc_precio:
            dicc_precio[clave] += v.precio
            dicc_aforo[clave] += v.aforo
            dicc_num[clave] += 1
        else:
            dicc_precio[clave] = v.precio
            dicc_aforo[clave] = v.aforo
            dicc_num[clave] = 1

    res = dict()
    for x in dicc_precio:
        res[x] = (dicc_precio[x] / dicc_num[x], dicc_aforo[x])
    
    return res









