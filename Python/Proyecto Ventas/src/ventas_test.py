from ventas import *

def lee_datos_ventas_test():
    print("Numero de elementos en el fichero: ", len(ventas))
    print("Datos de los primeros elementos del fichero:", ventas[:3])


def total_contratos_test():
    tupla = total_contratos(ventas, "Canarias")
    print("Total de contratos en la comunidad seleccionada: ", tupla)

def año_mas_contratos_por_llamadas_comunidad_test():
    tupla = año_mas_contratos_por_llamadas_comunidad(ventas, "Canarias")
    print("Año mas contratos por llamadas de la comunidad seleccionada: ", tupla)

def variaciones_anuales_contratos_test():
    tupla = variaciones_anuales_contratos(ventas, "Canarias")
    print("Variaciones anuales de contratos en la comunidad seleccionada:", tupla)

def año_mas_contratos_test():
    tupla = año_mas_contratos(ventas)
    print("Año mas contratos: ", tupla)

def agrupa_datos_por_años_test():
    tupla = agrupa_datos_por_años(ventas)
    print("Datos por año: ", tupla)


if __name__== '__main__':
    ventas = lee_datos_ventas('./data/ventas.csv')
    lee_datos_ventas_test()
    total_contratos_test()
    año_mas_contratos_por_llamadas_comunidad_test()
    variaciones_anuales_contratos_test()
    año_mas_contratos_test()
    agrupa_datos_por_años_test()


