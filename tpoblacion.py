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
        return [lambda x: x.getAptitud(), [x for x in range(0, self.tamPob)]]
