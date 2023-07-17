from reparaciones import *

def lee_reparaciones_test():
    print("El numero de elementos del CSV es: ", len(reparaciones))
    print("Las primeras 3 reparaciones son: ", reparaciones[:3])


def calcula_recaudacion_test():
    tupla = calcula_recaudacion(reparaciones, "Sevilla", None)
    print("Total recaudado con estos parametros: ", tupla)



def reparaciones_mas_largas_test():
    tupla = reparaciones_mas_largas(reparaciones, 2020, 3, None)
    print("Reparaciones mas largas con los parametros dados: ", tupla)

def centro_mas_rapido_test():
    tupla = centro_mas_rapido(reparaciones, "Sevilla, Cadiz, Huelva")
    print("Centro mas rapido: ", tupla)

def centros_experimentados_en_test():
    tupla = centros_experimentados_en(reparaciones, "la")
    print("Centros experimentados en: ", tupla)

def dias_entre_reparaciones_test():
    tupla = dias_entre_reparaciones(reparaciones)
    print("Dias entre reparaciones: ", tupla)


if __name__ == '__main__':
    reparaciones = lee_reparaciones('./data/reparaciones.csv')
    lee_reparaciones_test()
    calcula_recaudacion_test()
    reparaciones_mas_largas_test()
    centro_mas_rapido_test()
    centros_experimentados_en_test()
    dias_entre_reparaciones_test()