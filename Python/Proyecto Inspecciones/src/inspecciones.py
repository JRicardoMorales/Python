from collections import namedtuple
from collections import Counter
from datetime import datetime
from datetime import timedelta
from datetime import date
import csv

Inspeccion = namedtuple('Inspeccion', 'fecha_inspeccion, estacion, numero, fecha_limite, matricula, tipo, fecha_matriculacion, favorable')

'''
Funcion de lectura

'''

def lee_registros(fichero):
    datos = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for fecha_inspeccion, estacion, numero, fecha_limite, matricula, tipo, fecha_matriculacion, favorable in lector:
            fecha_inspeccion = datetime.strptime(fecha_inspeccion, '%d/%m/%Y').date()
            numero = int (numero)
            fecha_limite = datetime.strptime(fecha_limite, '%d/%m/%Y').date()
            fecha_matriculacion = datetime.strptime(fecha_matriculacion, '%d/%m/%Y').date()
            favorable = parse_bool(favorable)
            tupla = Inspeccion(fecha_inspeccion, estacion, numero, fecha_limite, matricula, tipo, fecha_matriculacion, favorable)
            datos.append(tupla)
    return datos

'''
Funcion auxiliar para la lectura

'''
def parse_bool(str_bool):
    res = False
    if str_bool == "S":
        res = True
    return res


'''
vehiculos mas antiguos

'''

def vehiculos_mas_antiguos(datos, año, n):
    inspecciones_año = [i for i in datos if i.fecha_inspeccion.year == año and i.favorable]
    inspecciones_año.sort(key = lambda i:i.fecha_matriculacion)
    matriculas = [i.matricula for i in inspecciones_año]
    return matriculas[:n]

'''
proximas inspecciones

'''

def proximas_inspecciones(datos):
    return [(i.matricula, calcula_fecha_proxima_inspeccion(i)) for i in datos if i.favorable]


def calcula_fecha_proxima_inspeccion(i):
    anyos = date.today().year - i.fecha_matriculacion.year
    if anyos <= 10:
        fecha = i.fecha_inspeccion + timedelta(2 * 365)
    else:
        fecha = i.fecha_inspeccion + timedelta(365)
    return fecha

'''
estacion_mayor_porcentaje_inspecciones_favorables

'''

def estacion_mayor_porcentaje_inspecciones_favorables(inspecciones, estaciones):
    diccionario_porcentajes = porcentaje_favorables_por_estacion(inspecciones, estaciones)
    return max(diccionario_porcentajes.items(), key = lambda e:e[1])


def porcentaje_favorables_por_estacion(inspecciones, estaciones):
    res = dict()
    for i in inspecciones:
        k = i.estacion
        if i.estacion in estaciones:
            if k in res:
                res[k].append(i)
            else:
                res[k] = [i]
    for estacion, lista_inspecciones in res.items():
        res[estacion] = len([i for i in lista_inspecciones if i.favorable]) * 100 / len(lista_inspecciones)
    return res



'''
tipos_de_vehiculos_mas_inspeccionados

'''

def tipos_de_vehiculos_mas_inspeccionados (inspecciones, f1, f2):
    d = agrupar_por_estacion_en_fechas(inspecciones, f1, f2)
    return {estacion: mayor_tipo_vehiculo(inspecciones) for estacion, inspecciones in d.items()}


def agrupar_por_estacion_en_fechas(inspecciones, f1, f2):
    d = dict()
    for i in inspecciones:
        if esta_en_fechas(i, f1, f2):
            if i.estacion in d:
                d[i.estacion].append(i)
            else:
                d[i.estacion] = [i]
    return d


def esta_en_fechas(i, f1, f2):
    res = True
    if f1 != None and f2 != None:
        res = f1 < i.fecha_inspeccion < f2
    elif f1 == None and f2 != None:
        res = i.fecha_inspeccion < f2
    elif f2==None and f1 != None:
        res = f1 < i.fecha_inspeccion
    return res


def mayor_tipo_vehiculo(inspecciones):
    c = Counter(i.tipo for i in inspecciones)
    return c.most_common(1)[0][0]



'''
incrementos_recaudacion_estacion

'''

def incrementos_recaudacion_estacion(inspecciones, estacion):
    año_min = min(i.fecha_inspeccion.year for i in inspecciones)
    año_max = max(i.fecha_inspeccion.year for i in inspecciones)

    años = [y for y in range(año_min, año_max+1)]
    dicc_recaudaciones = {a: 0 for a in años}
    for i in inspecciones:
        if i.estacion == estacion:
            k = i.fecha_inspeccion.year
            if k in dicc_recaudaciones:
                dicc_recaudaciones[k] += importe_inspeccion(i)
            else:
                dicc_recaudaciones[k] = importe_inspeccion(i)
    recaudaciones = [r for _, r in sorted(dicc_recaudaciones.items())]
    incrementos = [r2 - r1 for r1, r2 in zip(recaudaciones, recaudaciones[1:])]
    return incrementos


def importe_inspeccion(inspeccion):
    res = 0
    if inspeccion.tipo == 'Turismo gasolina':
        importe = 24.05
    elif inspeccion.tipo == 'Turismo diésel':
        importe = 28.27
    elif inspeccion.tipo == 'Turismo eléctrico':
        importe = 20.60
    if inspeccion.fecha_inspeccion < inspeccion.fecha_limite:
        importe = importe - importe * 0.10
    elif inspeccion.fecha_inspeccion > inspeccion.fecha_limite + timedelta(30):
        importe = importe + importe * 0.12
    if inspeccion.numero >= 3:
        importe += 9.11
    importe *= 1.21
    importe += 4.18
    return importe


    






