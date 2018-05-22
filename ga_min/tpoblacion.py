from tindividuo import TIndividuo
from copy import deepcopy

# import numpy as np
# import matplotlib as plt


class TPoblacion:

    def __init__(self, tamPob, lcrom, x_min, x_max):
        self.tamPob = tamPob
        self.lcrom = lcrom
        self.x_min = x_min
        self.x_max = x_max
        self.pob = [TIndividuo(lcrom, x_min, x_max) for i in range(0, tamPob)]

    def getAdaptaciones(self):
        return [x.x for x in self.pob], [x.aptitud_bruta for x in self.pob]

    def evaluacion(self):
        self.revisar_adap_mini()
        punt_acu = 0.0     # puntuación acumulada de los individuos
        aptitud_mejor = 0.0   # mejor aptitud
        self.sumaptitud = 0.0     # suma del aptitud

        for i in range(0, self.tamPob):
            self.sumaptitud += self.pob[i].aptitud
            if self.pob[i].aptitud > aptitud_mejor:
                self.pos_mejor = i
                aptitud_mejor = self.pob[i].aptitud

        for i in range(0, self.tamPob):
            self.pob[i].puntuacion = self.pob[i].aptitud / self.sumaptitud
            self.pob[i].punt_acu = self.pob[i].puntuacion + punt_acu
            punt_acu += self.pob[i].puntuacion

    def muestraPoblacion(self):
        self.evaluacion()
        for i in range(0, self.tamPob):
            print("ind {} x={}, "
                  "aptitud={},"
                  "elite={}".format(i, self.pob[i].x, self.pob[i].getAptitud(),
                                    self.pob[i].elite))

    def muestraMejor(self):
        self.evaluacion()
        print("ind {} x={}, aptitud={}".format(
            self.pos_mejor, self.pob[self.pos_mejor].x,
            self.pob[self.pos_mejor].getAptitud()))

    def retornaPoblacion(self):
        return self.pob

    def clone(self):
        return deepcopy(self)

    def revisar_adap_mini(self):
        cmax = self.pob[0].aptitud_bruta
        for i in self.pob:
            if hasattr(i, 'aptitud'):
                if i.aptitud > cmax:
                    cmax = i.aptitud_bruta

        cmax = cmax + cmax / 100
        for i in self.pob:
            i.aptitud = cmax - i.aptitud_bruta
