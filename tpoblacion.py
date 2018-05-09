from tindividuo import TIndividuo
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
        return [x.getAptitud() for x in self.pob]

    def evaluacion(self):
        punt_acu = 0.0     # puntuación acumulada de los individuos
        aptitud_mejor = 0.0   # mejor aptitud
        self.sumaptitud = 0.0     # suma del aptitud

        for i in range(0, self.tamPob):
            self.sumaptitud += self.pob[i].getAptitud()
            if self.pob[i].getAptitud() > aptitud_mejor:
                self.pos_mejor = i
                aptitud_mejor = self.pob[i].getAptitud()

        for i in range(0, self.tamPob):
            self.pob[i].puntuacion = self.pob[i].getAptitud()/self.sumaptitud
            self.pob[i].punt_acu = self.pob[i].puntuacion + punt_acu
            punt_acu += self.pob[i].puntuacion

        print(self.pos_mejor, "aptitud= ", aptitud_mejor)
