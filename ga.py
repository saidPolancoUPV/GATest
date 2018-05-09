import argparse
from math import ceil, log
from tpoblacion import TPoblacion
from testFuncObjet import Display

# Se obtienen los parámetros por medio de la línea de comandos
parser = argparse.ArgumentParser(description="Algoritmo genético simple")
parser.add_argument("x_max", type=float, help="Límite superior del segmento")
parser.add_argument("x_min", type=float, help="Límite infeior del segmento")
parser.add_argument("tol", type=float, help="Exactitud o tolerancia : 0.000x")
parser.add_argument("tamPob", type=int, help="Tamaño de la población")

args = parser.parse_args()   # se obtiene el objeto

# x_max = int(input("Ingresa el límite superior: "))
# x_min = int(input("Ingresa el límite inferior: "))
# TOL = float(input("Ingresa la tolerancia: "))

# Calculamos el largo del cromosoma
lcrom = ceil(log(1 + ((args.x_max - args.x_min)/args.tol), 2))

# 1.- Se genera la población inicial. (cada individuo se auto evalua)
pob = TPoblacion(args.tamPob, lcrom, args.x_min, args.x_max)

# 2.- Se evalua la población
pob.evaluacion()
