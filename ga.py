from math import ceil, log
from tpoblacion import TPoblacion
from testFuncObjet import Display

x_max = int(input("Ingresa el límite superior: "))
x_min = int(input("Ingresa el límite inferior: "))
TOL = float(input("Ingresa la tolerancia: "))

lcrom = ceil(log(1 + ((x_max - x_min)/TOL), 2))

pob = TPoblacion(10, lcrom, x_min, x_max)

print(pob.getAdaptaciones())

# d = Display()

# d.disp(x_min, x_max, TOL)
