from inspecciones import *



def lee_inspecciones_test():
    print("El numero de elementos que hay en el csv es: ", len(inspecciones))
    print(inspecciones[:5])

def vehiculos_mas_antiguos_test():
    tupla = vehiculos_mas_antiguos(inspecciones, 2022, 3)
    print("Vehiculos mas antiguos:", tupla)

def proximas_inspecciones_test():
    tupla = proximas_inspecciones(inspecciones)
    print("Proximas inspecciones", tupla)

def estacion_mayor_porcentaje_inspecciones_favorables_test():
    tupla = estacion_mayor_porcentaje_inspecciones_favorables(inspecciones, "Sevilla-Gelves, La Rinconada")
    print("Estacion mayor porcentaje inspecciones favorables: ", tupla)

def tipos_de_vehiculos_mas_inspeccionados_test():
    tupla = tipos_de_vehiculos_mas_inspeccionados(inspecciones, None, None)
    print("Vehiculos mas inspeccionados entre dos fechas: ", tupla)

def incrementos_recaudacion_estacion_test():
    tupla = incrementos_recaudacion_estacion(inspecciones, "Sevilla-Gelves" )
    print("Incrementos recaudaciones", tupla)






if __name__ == '__main__':
    inspecciones = lee_registros("./data/inspecciones.csv")
    lee_inspecciones_test()
    vehiculos_mas_antiguos_test()
    proximas_inspecciones_test()
    estacion_mayor_porcentaje_inspecciones_favorables_test()
    tipos_de_vehiculos_mas_inspeccionados_test()
    incrementos_recaudacion_estacion_test()