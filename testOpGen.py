from copergen import COperGen
from tpoblacion import TPoblacion

p = TPoblacion(100, 5, 0.0, 32.0)
p.evaluacion()
og = COperGen()
og.obtenPoblacion(p.clone())
og.seleccion()
# for i in og.pob:
#    print("x={}, aptitud={}, elite={}, "
#          "puntuacion_acu={}".format(i.x, i.getAptitud(),
#                                   int(i.elite), i.punt_acu))
